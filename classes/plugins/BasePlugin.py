from threading import Thread

from classes.APIConnector import APIConnector
from classes.Character import Character
from classes.PhBot import PhBot, logger
from classes.plugins.Config import Config


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as err:
            logger.exception(err, extra={'plugin': func.__name__})

    return inner_function


class BasePlugin(object):
    def __init__(self, plugin_name=None, token=None, config=None):
        self.bot = PhBot(plugin_name=plugin_name)
        self.api = APIConnector(bot=self.bot, token=token)
        self.loop_buffers = {}

        self.plugin_name = plugin_name

        self.config: Config = None
        self.char = Character()

    def set_char(self, char: Character):
        self.char = char

    def set_config(self):
        self.config = Config(self.bot.get_config_dir(), self.char, self.plugin_name)

    def run_thread(self, fnc, args=(), delay=5):
        fnc_name = fnc.__name__

        if not self.loop_buffers.get(fnc_name, None):
            self.loop_buffers[fnc_name] = 0

        if self.loop_buffers[fnc_name] < delay + 2:
            self.loop_buffers[fnc_name] += 1
            return

        t = Thread(target=fnc, args=args)
        t.start()

        del self.loop_buffers[fnc_name]

    def event_loop(self):
        pass

    def joined_game(self):
        pass

    def handle_event(self, t, data):
        pass

    def handle_joymax(self, opcode, data):
        pass

    def handle_chat(self, t, player, msg):
        pass

    def setup(self):
        pass

    @exception_handler
    def initialize(self):
        if not self.char.is_joined():
            char_info = self.bot.get_character_data()
            if char_info:
                char = Character()
                char.set(char_info)
                self.set_char(char)
                self.set_config()
