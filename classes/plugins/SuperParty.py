import struct

from Plugins.classes.PhBot import EVENT_HUNTER_SPAWN
from classes.plugins.BasePlugin import BasePlugin, exception_handler


class SuperParty(BasePlugin):
    def __init__(self, gui=None):
        """This is a helper plugin for 7/24 afk parties."""

        super().__init__(
            plugin_name=self.__class__.__name__,
        )

        self.gui = gui
        self.detect_hunters_checkbox = None
        self.party_data = None

    @exception_handler
    def handle_event(self, t, data):
        # if char is in training area.
        if (not self.char) and self.bot.in_training_area():
            return
        if t == EVENT_HUNTER_SPAWN and self.config.get('detect_hunters'):
            self.notify('Hunter is near!', 'Hunter name: {}'.format(data))

    @exception_handler
    def handle_joymax(self, opcode, data):
        if (not self.char) and (not self.bot.in_training_area()):
            return

        elif opcode == 0x3065:
            self.bot.log_to_file(self.party_data)

            if self.party_data:
                old_party_data = self.party_data
                self.party_data = self.bot.get_party()
                if len(self.party_data) > len(old_party_data):
                    self.bot.log('There is new player in the PT.')
                    self.notify('There is new player in the PT.')
            else:
                self.party_data = self.bot.get_party()

            self.bot.log_to_file("@@@@@@@@@@@@")
            self.bot.log_to_file(self.party_data)

        if opcode == 0x3864:
            if self.party_data:
                update_type = data[0]
                if update_type == 1:
                    self.notify('Party Update', 'You left the party!')

                elif update_type == 2:
                    self.notify('Party Update', 'Someone joined the pt!')
                    self.party_data = self.bot.get_party()
                    member_name_length = struct.unpack_from('<H', data, 6)[0]
                    member_name = struct.unpack_from('<' + str(member_name_length) + 's', data, 8)[0].decode('cp1252')
                    self.notify('New Party Member', '{}\'s joined to party.'.format(member_name))

                elif update_type == 3:
                    self.bot.log("someone left the pt")
                    join_id = struct.unpack_from("<I", data, 1)[0]
                    member = self.party_data.get(join_id, None)
                    if member:
                        member_name = member['name']
                        self.notify('Party Member Left', '{}\'s left the party.'.format(member_name))

                elif update_type == 6:  # update member
                    if data[5] == 2:  # level
                        self.bot.log("someone leveled up")
                        join_id = struct.unpack_from("<I", data, 1)[0]
                        new_level = data[6]
                        member = self.party_data.get(join_id, None)
                        if member:
                            old_level = member['level']
                            self.party_data[join_id]['level'] = new_level
                            if old_level < new_level:
                                self.notify(
                                    'Party Member Leveled Up!',
                                    '{}\'s left the party.'.format(self.party_data[join_id]['name'])
                                )

    def notify(self, title: str, text: str):
        self.bot.log('Discord message sent: {}'.format(text))

    @exception_handler
    def setup(self):
        self.initialize()

        self.bot.qt.createLabel(self.gui, self.__init__.__doc__, 10, 10)
        self.detect_hunters_checkbox = self.bot.qt.createCheckBox(self.gui, 'save_config', 'Notify if Hunter around',
                                                                  10,
                                                                  30)

        # Set initial values
        self.bot.qt.setChecked(
            self.gui,
            self.detect_hunters_checkbox,
            self.config.get('detect_hunters', True)
        )

        self.bot.qt.createButton(self.gui, 'start_bot', 'Start Bot', 10, 250)

        self.bot.log('loaded')

    def save_config(self, *args):
        self.config.set('detect_hunters', self.bot.qt.isChecked(self.gui, self.detect_hunters_checkbox))
        self.bot.log('Saving configs')
