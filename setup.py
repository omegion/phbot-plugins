import json
import os
import shutil
import urllib
import urllib.request
from io import BytesIO
from threading import Timer
from typing import Optional

GITHUB_REPO = "omegion/phbot-plugins"
GITHUB_LATEST_RELEASE_URL = "https://github.com/{}/releases/latest/download/classes.zip".format(GITHUB_REPO)

PLUGIN_FOLDER = "Plugins"
CLASSES_PATH = os.path.join(os.getcwd(), PLUGIN_FOLDER)


class Setup(object):
    def __init__(self):
        """This is a setup plugin for managing other supported plugins."""

        self.plugin_folder = 'Plugins'
        self.headers = {
            'content-type': 'application/json',
        }

    def save(self):
        try:
            from classes import VERSION
            latest_version = self.get_latest_version()
            if VERSION != latest_version:
                self.download()
        except ImportError:
            self.download()

    def download(self) -> None:
        req = urllib.request.Request(GITHUB_LATEST_RELEASE_URL, headers=self.headers)
        try:
            resp = urllib.request.urlopen(req)
            self._clean_up_folder()
            self._extract_files(zipfile.ZipFile(BytesIO(resp.read())))
        except Exception as err:
            pass

    def get_latest_version(self) -> Optional[str]:
        url = "https://api.github.com/repos/{}/releases/latest".format(GITHUB_REPO)
        req = urllib.request.Request(url, headers=self.headers)
        try:
            resp = urllib.request.urlopen(req)
        except Exception as err:
            return None

        body = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
        return body.get('tag_name', None)

    def _validate(self) -> None:
        try:
            from classes import VERSION
            latest_version = self.get_latest_version()
            if VERSION == latest_version:
                print('Classes has updated.')
        except ImportError:
            pass

    def _clean_up_folder(self) -> None:
        shutil.rmtree(CLASSES_PATH + '/classes')

    def _extract_files(self, zip_file) -> None:
        t = Timer(1.0, lambda: zip_file.extractall(CLASSES_PATH))
        t.start()
