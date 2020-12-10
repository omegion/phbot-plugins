import json
import os

from classes.Character import Character

CONFIG_DIR_NAME = "plugins_config"


class Config(object):
    def __init__(self, config_path=None, char: Character = None, plugin_name=None):
        self.config_path = config_path
        self.char = char
        self.plugin_name = plugin_name

        self.data = {}
        if char:
            self.data = self.init_config_file()

    def get_path(self):
        return "{}{}\\{}.{}.json".format(
            self.config_path,
            CONFIG_DIR_NAME,
            self.char.server,
            self.char.name,
        )

    def set(self, key: str, value):
        self.data[key] = value
        config_data = self._read_config_file()
        config_data[self.plugin_name] = self.data
        self._write_to_config_file(config_data)

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def init_config_file(self):
        if os.path.exists(self.get_path()):
            config_data = self._read_config_file()
            data = config_data.get(self.plugin_name, None)
            if data is None:
                data = {}
        else:
            config_path = "{}{}".format(self.config_path, CONFIG_DIR_NAME)
            if not os.path.exists(config_path):
                os.makedirs(config_path)
            config_data = {self.plugin_name: {}}
            self._write_to_config_file(config_data)
            data = {}

        return data

    def _read_config_file(self):
        with open(self.get_path(), 'r') as f:
            return json.load(f)

    def _write_to_config_file(self, config_data):
        with open(self.get_path(), "w") as f:
            f.write(json.dumps(config_data, indent=4, sort_keys=True))
