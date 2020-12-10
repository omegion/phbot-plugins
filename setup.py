import glob
import json
import os
import shutil
import urllib
import urllib.request
import zipfile
from io import BytesIO
from threading import Timer
from typing import Optional

import QtBind
from phBot import log

GITHUB_REPO = "omegion/phbot-plugins"
GITHUB_LATEST_RELEASE_URL = "https://github.com/{}/releases/latest/download/classes.zip".format(GITHUB_REPO)

PLUGINS_FOLDER_NAME = "Plugins"
PLUGINS_PATH = os.path.join(os.getcwd(), PLUGINS_FOLDER_NAME)

ACTIVE_PLUGINS = [
    {
        'id': None,
        'name': 'o_control',
        'description': 'A Control plugin to help control your bot with in-game chat.',
    },
    {
        'id': None,
        'name': 'o_ch_force_helper',
        'description': 'A helper plugin for CH force chars.',
    },
]


class Setup(object):
    def __init__(self, gui=None):
        """This is a setup plugin for managing other supported plugins."""

        self.gui = gui
        self.installed_plugins = []
        self.headers = {
            'content-type': 'application/json',
        }

    def install_plugins(self):
        latest_version = plugin.install_classes()
        for key, element in enumerate(ACTIVE_PLUGINS):
            if QtBind.isChecked(gui, ACTIVE_PLUGINS[key]['id']):
                plugin.download_plugin(element.get('name'), latest_version)

    def install_classes(self) -> str:
        latest_version = self.get_latest_version()
        try:
            from classes import VERSION
            if VERSION != latest_version:
                self.log('Classes has new version {}, will update.'.format(latest_version))
                self.download_classes()
        except ImportError:
            self.log('Classes could not found, will download.')
            self.download_classes()

        return latest_version

    def download_classes(self) -> None:
        req = urllib.request.Request(GITHUB_LATEST_RELEASE_URL, headers=self.headers)
        try:
            resp = urllib.request.urlopen(req)
            self._clean_up_folder()
            self._extract_files(zipfile.ZipFile(BytesIO(resp.read())))
            self.log('Classes updated.')
        except Exception as err:
            self.log(err)

    def download_plugin(self, plugin_name: str, classes_version: str) -> None:
        url = "https://raw.githubusercontent.com/omegion/phbot-plugins/{}/{}.py".format(
            classes_version,
            plugin_name
        )
        try:
            urllib.request.urlretrieve(url, "{}/{}.py".format(PLUGINS_PATH, plugin_name))
            self.log('{} installed.'.format(plugin_name))
        except Exception as err:
            self.log('{} could not be installed'.format(plugin_name))

    def get_latest_version(self) -> Optional[str]:
        url = "https://api.github.com/repos/{}/releases/latest".format(GITHUB_REPO)
        req = urllib.request.Request(url, headers=self.headers)
        try:
            resp = urllib.request.urlopen(req)
        except Exception as err:
            return "master"

        body = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
        return body.get('tag_name', None)

    def setup(self):
        self._detect_installed_plugins()

        QtBind.createLabel(self.gui, self.__init__.__doc__, 10, 10)
        QtBind.createButton(gui, 'install_plugins', "Install/Update Plugins", 10, len(ACTIVE_PLUGINS) * 32)

        for key, element in enumerate(ACTIVE_PLUGINS):
            ACTIVE_PLUGINS[key]['id'] = QtBind.createCheckBox(gui, 'empty', element.get('description'), 10,
                                                              (20 * (key + 1)))
            if ACTIVE_PLUGINS[key]['name'] in self.installed_plugins:
                QtBind.setChecked(gui, ACTIVE_PLUGINS[key]['id'], True)

    def log(self, text):
        log("{}: {}".format('Setup Plugin', text))

    def _detect_installed_plugins(self) -> None:
        plugins = glob.glob(PLUGINS_PATH + "/o_*.py")
        for plugin in plugins:
            plugin_name = os.path.splitext(os.path.basename(plugin))[0]
            self.installed_plugins.append(plugin_name)

    def _validate(self) -> None:
        try:
            from classes import VERSION
            latest_version = self.get_latest_version()
            if VERSION == latest_version:
                self.log('classes has updated.')
        except ImportError:
            pass

    def _clean_up_folder(self) -> None:
        classes_path = os.path.join(PLUGINS_PATH, 'classes')
        if os.path.exists(classes_path):
            shutil.rmtree(classes_path)

    def _extract_files(self, zip_file) -> None:
        zip_file.extractall(PLUGINS_PATH)


gui = QtBind.init(__name__, Setup.__name__)

plugin = Setup(
    gui=gui,
)

plugin.setup()


def install_plugins(*args, **kwargs):
    t = Timer(0.0, lambda: plugin.install_plugins())
    t.start()
