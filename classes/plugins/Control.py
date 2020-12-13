from urllib import parse
from urllib.parse import parse_qs

from classes import VERSION
from classes.plugins.BasePlugin import BasePlugin, exception_handler

COMMANDS = [
    {
        'name': 'START',
        'description': 'Starts the bot',
        'arguments': []
    },
    {
        'name': 'STOP',
        'description': 'Stops the bot',
        'arguments': []
    },
    {
        'name': 'SETAREA',
        'description': 'Sets new training area with name "default".',
        'arguments': ['x', 'y', 'region', 'r']
    },
    {
        'name': 'SETRADIUS',
        'description': 'Sets new new radius value for "default".',
        'arguments': ['r']
    },
    {
        'name': 'RETURN TOWN',
        'description': 'Uses return scroll',
        'arguments': []
    },
    {
        'name': 'STATUS',
        'description': 'Shows bot status.',
        'arguments': []
    },
    {
        'name': 'VERSION',
        'description': 'Shows bot and plugin versions.',
        'arguments': []
    },
]


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
        self.bot.qt.createLabel(self.gui, self.__init__.__doc__, 10, 10)
        self.bot.qt.createLabel(self.gui, VERSION, 680, 270)
        self.leader_input = self.bot.qt.createLineEdit(self.gui, "", 10, 30, 100, 20)
        self.leaders_list = self.bot.qt.createList(self.gui, 10, 58, 175, 48)
        self.bot.qt.createButton(self.gui, 'add_leader_button_action', "Add", 112, 28)
        self.bot.qt.createButton(self.gui, 'remove_leader_button_action', "Remove", 10, 110)
        self.bot.qt.createButton(self.gui, 'get_position_button_action', "Get Position", 10, 255)
        self._command_labels()

        if self.char.is_joined():
            self._load_leaders_from_config()

    @exception_handler
    def joined_game(self):
        self.initialize()
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

            elif msg.startswith("SETRADIUS"):
                self._set_radius(t, player, msg)

            elif msg.startswith("RETURN TOWN"):
                self._return_town(t, player, msg)

            elif msg.startswith("STATUS"):
                self._status(t, player, msg)

            elif msg.startswith("VERSION"):
                self._version(t, player, msg)

    def add_leader(self):
        player = self.bot.qt.text(self.gui, self.leader_input)

        if player:
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

    def get_position(self):
        pos = self.bot.get_position()
        if pos:
            self.bot.log(
                "Current position: X: %.0f, Y: %.0f, Z: %.0f, Region: %d" %
                (pos['x'], pos['y'], pos['z'], pos['region'])
            )

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
        if not params.get('x', None) or not params.get('y', None) or not params.get('y', None):
            self._send_response('X, Y or Region is missing', t, player, msg)
            return

        x = int(params.get('x'))
        y = int(params.get('y'))
        region = int(params.get('region'))
        radius = int(params.get('r', 30))

        bot_config = self.bot.get_config()

        # set other training areas default
        for training_area_name in bot_config['Loop']['Script']:
            bot_config['Loop']['Script'][training_area_name]['Enabled'] = False

        bot_config['Loop']['Script']['default'] = {
            "Data": [],
            "Enabled": True,
            "Path": "",
            "Pick Radius": 50,
            "Radius": radius,
            "Region": region,
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

    def _set_radius(self, t, player, msg):
        params = self._parse_message_arguments(msg)
        if not params.get('r', None):
            self._send_response('R is missing', t, player, msg)
            return

        r = int(params.get('r'))

        self.bot.set_training_radius(r)

        self._send_response('Radius set to %d' % r, t, player, msg)

    def _return_town(self, t, player, msg):
        character = self.bot.get_character_data()
        if character['hp'] == 0:
            self.bot.inject_joymax(0x3053, b'\x01', False)
        else:
            self.bot.use_return_scroll()
        self._send_response('Returning to town', t, player, msg)

    def _status(self, t, player, msg):
        status = {
            'bot': True if self.bot.get_status() else False,
        }
        response = "Botting: %s" % status['bot']
        self._send_response(str(response), t, player, msg)

    def _version(self, t, player, msg):
        status = {
            'bot': self.bot.get_version(),
            'plugin': VERSION
        }
        response = "Bot: %s, Plugin: %s" % (status['bot'], status['plugin'])
        self._send_response(str(response), t, player, msg)

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

    def _command_labels(self):
        for key, command in enumerate(COMMANDS):
            description = "%s" % command['name']
            if len(command['arguments']):
                description += '(' + ', '.join(command['arguments']) + ')'

            description += ': %s' % command['description']
            self.bot.qt.createLabel(self.gui, description, 210, (28 * (key + 1)))
