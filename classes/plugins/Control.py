from urllib import parse
from urllib.parse import parse_qs

from classes.plugins.BasePlugin import BasePlugin, exception_handler


class Control(BasePlugin):
    def __init__(self, gui=None):
        """This is a plugin to control the bot from in-game chat"""

        super().__init__(
            plugin_name=self.__class__.__name__,
        )

        self.gui = gui
        self.leader_input = None
        self.leaders_list = None

    @exception_handler
    def setup(self):
        self.initialize()

        # GUI Inits
        self.bot.qt.createButton(self.gui, 'test', 'Test', 10, 250)
        self.leader_input = self.bot.qt.createLineEdit(self.gui, "", 511, 11, 100, 20)
        self.leaders_list = self.bot.qt.createList(self.gui, 511, 32, 176, 48)
        self.bot.qt.createButton(self.gui, 'add_leader_button_action', "Add", 612, 10)
        self.bot.qt.createButton(self.gui, 'remove_leader_button_action', "Remove", 560, 79)

        # Config
        self._load_leaders_from_config()

    @exception_handler
    def handle_chat(self, t, player, msg):
        if player and self._is_leader(player):
            if msg == 'START':
                self._start_command(t, player, msg)

            elif msg == 'STOP':
                self._stop_command(t, player, msg)

            elif msg.startswith("SETAREA"):
                self._set_area(t, player, msg)

            elif msg.startswith("RETURN TOWN"):
                self._return_town(t, player, msg)

    def add_leader(self):
        player = self.bot.qt.text(self.gui, self.leader_input)

        leaders = self.config.get('leaders')
        if leaders:
            leaders.append(player)
        else:
            leaders = [player]

        self.config.set('leaders', leaders)
        self.bot.qt.append(self.gui, self.leaders_list, player)
        self.bot.qt.setText(self.gui, self.leader_input, "")

    def remove_leader(self):
        selected_leader = self.bot.qt.text(self.gui, self.leaders_list)
        if selected_leader:
            leaders = self.config.get('leaders')
            if leaders:
                leaders.remove(selected_leader)
                self.config.set('leaders', leaders)
                self.bot.qt.remove(self.gui, self.leaders_list, selected_leader)

    def _load_leaders_from_config(self):
        leaders = self.config.get('leaders')
        if leaders:
            for leader in leaders:
                self.bot.qt.append(self.gui, self.leaders_list, leader)

    def _is_leader(self, player) -> bool:
        leaders = self.config.get('leaders')
        if leaders:
            return player in leaders

    def _start_command(self, t, player, msg):
        self.bot.start()
        self._send_response('Started the bot', t, player, msg)

    def _stop_command(self, t, player, msg):
        self.bot.stop()
        self._send_response('Stopped the bot', t, player, msg)

    def _set_area(self, t, player, msg):
        params = self._parse_message_arguments(msg)
        if not params.get('x', None) or not params.get('y', None):
            self._send_response('X or Y missing', t, player, msg)
            return

        x = int(params.get('x'))
        y = int(params.get('y'))
        radius = int(params.get('r', 30))

        bot_config = self.bot.get_config()

        # set other training areas default
        for training_area_name in bot_config['Loop']['Script']:
            bot_config['Loop']['Script'][training_area_name]['Enabled'] = False

        bot_config['Loop']['Script']['default'] = {
            "Enabled": True,
            "Path": "",
            "Pick Radius": 50,
            "Radius": radius,
            "Region": 0,
            "Type": 0,
            "X": x,
            "Y": y,
            "Z": 0
        }

        self.bot.set_config(bot_config)
        self.bot.reload_config()
        self._send_response(
            'Training area set to: (x: {}, y: {}, r:{})'.format(
                params.get('x', None),
                params.get('y', None),
                params.get('r', 30)),
            t,
            player,
            msg
        )

        pass

    def _return_town(self, t, player, msg):
        self.bot.use_return_scroll()
        self._send_response('Returning to town', t, player, msg)

    def _send_response(self, text, t, player, msg):
        self.bot.log(text)
        if t == 4:
            self.bot.chat.Party(text)
            return
        self.bot.chat.Private(player, text)

    def _parse_message_arguments(self, message) -> dict:
        corrected_message = message.replace(' ', '&')
        query = parse.urlsplit("?" + corrected_message).query
        parameters = dict(parse_qs(query))
        return {k: v[0] for k, v in parameters.items()}
