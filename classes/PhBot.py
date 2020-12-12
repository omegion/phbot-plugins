import json
import logging
import math
import os
import sqlite3
from sqlite3 import Error
from threading import Timer

from classes.Chatter import Chatter

logging.basicConfig(filename=os.path.join('Plugins', 'plugin.log'), level=logging.DEBUG,
                    format='%(asctime)s %(threadName)s %(plugin)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

EVENT_UNIQUE_SPAWN = 0  # data = monster name
EVENT_HUNTER_SPAWN = 1  # data = player name (includes traders)
EVENT_THIEF_SPAWN = 2  # data = player name
EVENT_TRANSPORT_DIED = 3  # data = transport id (includes horses)
EVENT_PLAYER_ATTACKING = 4  # data = player name
EVENT_RARE_DROP = 5  # data = item model (equippable only)
EVENT_ITEM_DROP = 6  # data = item model (equippable only)
EVENT_DIED = 7  # data = empty string
EVENT_ALCHEMY_FINISHED = 8  # data = empty string
EVENT_GM_SPAWNED = 9  # data = player name


class PhBot(object):
    def __init__(self, plugin_name=None):
        self.bot = self._get_bot()
        self.qt = self._get_qt()
        self.db = self._get_db()
        self.chat = self._get_chat()
        self.plugin_name = plugin_name

    # CONFIG
    def get_config(self):
        with open(self.get_config_path(), 'r') as f:
            return json.load(f)

    def set_config(self, config: dict):
        with open(self.get_config_path(), "w") as f:
            f.write(json.dumps(config, indent=4, sort_keys=True))

    # DATABASE
    def db_update_pick_filter(self):
        pass

    def get_db_file(self):
        if self.bot:
            self.get_startup_data()
            startup_data = self.get_startup_data()
            if startup_data:
                return "{}{}_{}.db3".format(
                    self.get_config_dir(),
                    startup_data['server'],
                    startup_data['character']
                )
        return None

    # NATIVE METHODS
    def stop(self):
        if self.bot:
            self.bot.stop_bot()
            return True
        return None

    def start(self, delay=None):
        if self.bot:
            if delay:
                t = Timer(delay, lambda: self.bot.start_bot())
                t.start()
            else:
                self.bot.start_bot()
            return True
        return None

    def reload_config(self):
        if self.bot:
            current_profile = self.bot.get_profile()
            self.bot.set_profile(current_profile)
            return True
        return None

    def use_return_scroll(self):
        if self.bot:
            self.bot.use_return_scroll()
            return True
        return None

    def set_profile(self, profile_name):
        if self.bot:
            self.bot.set_profile(profile_name)
            return True
        return None

    def set_training_radius(self, r):
        if self.bot:
            self.bot.set_training_radius(r)
            return True
        return None

    def get_job_pouch(self):
        if self.bot:
            return self.bot.get_job_pouch()
        return None

    def get_config_dir(self):
        if self.bot:
            return self.bot.get_config_dir()
        return None

    def get_config_path(self):
        if self.bot:
            return self.bot.get_config_path()
        return None

    def get_character_data(self):
        if self.bot:
            return self.bot.get_character_data()
        return None

    def get_party(self):
        if self.bot:
            return self.bot.get_party()
        return None

    def get_active_skills(self):
        if self.bot:
            return self.bot.get_active_skills()
        return None

    def get_training_position(self):
        if self.bot:
            return self.bot.get_training_position()
        return {'x': 50.0, 'y': 50.0, 'radius': 100.0}

    def get_position(self):
        if self.bot:
            return self.bot.get_position()
        return {
            'region': 0,
            'z': 0,
            'y': 50.0,
            'x': 50.0
        }

    def get_profile(self):
        if self.bot:
            return self.bot.get_profile()
        return None

    def get_startup_data(self):
        if self.bot:
            return self.bot.get_startup_data()
        return None

    def get_status(self):
        if self.bot:
            return self.bot.get_status()
        return None

    def get_drops(self):
        if self.bot:
            return self.bot.get_drops()
        return None

    def get_client(self):
        if self.bot:
            return self.bot.get_client()
        return None

    def get_version(self):
        if self.bot:
            return self.bot.get_version()
        return None

    def start_trace(self, char_name):
        if self.bot:
            return self.bot.start_trace(char_name)
        return None

    def stop_trace(self):
        if self.bot:
            return self.bot.stop_trace()
        return None

    def generate_path(self, x, y):
        if self.bot:
            return self.bot.generate_path(x, y)
        return None

    def inject_joymax(self, opcode, data, encrypted):
        if self.bot:
            return self.bot.inject_joymax(opcode, data, encrypted)
        return None

    # GUI
    def set_text(self, *args):
        if self.qt:
            self.qt.setText(*args)
            return True
        return None

    def log(self, text):
        log_text = "{}: {}".format(
            self.plugin_name,
            str(text)
        )
        if self.bot:
            self.bot.log(log_text)
        else:
            logger.debug(log_text)

    def log_to_file(self, text):
        logger.info(text, extra={'plugin': self.plugin_name})

    def exception(self, e):
        logger.exception(e, extra={'plugin': self.plugin_name})

    def in_training_area(self):
        training_pos = self.get_training_position()
        char_pos = self.get_position()

        dist = math.sqrt(
            (training_pos['x'] - char_pos['x']) ** 2 + (training_pos['y'] - char_pos['y']) ** 2
        )

        return dist <= training_pos['radius']

    def _get_bot(self):
        try:
            import phBot
            return phBot
        except ImportError:
            return None

    def _get_qt(self):
        try:
            import QtBind
            return QtBind
        except ImportError:
            return None

    def _get_db(self):
        db_file = self.get_db_file()
        if db_file:
            conn = None
            try:
                conn = sqlite3.connect(db_file, check_same_thread=False)
            except Error as e:
                self.exception(e)

            return conn
        return None

    def _get_chat(self):
        return Chatter().get_chatter()
