import urllib
import urllib.request

import QtBind
from phBot import *

gui = QtBind.init(__name__, 'Reload Config')

QtBind.createLabel(gui,
                   'Welcome to the Reload Config',
                   10, 10)

reload_button = QtBind.createButton(gui, 'generate', 'Generate', 10, 30)


def generate():
    # set_profile(get_profile())
    download()
    log('Profile reloaded.')


def download():
    url = "https://github.com/omegion/phbot-plugins/releases/download/v0.0.1/classes.zip"
    req = urllib.request.Request(url)
    try:
        mp3file = urllib.request.urlopen(req)
        with open('classes.zip', 'wb') as output:
            output.write(mp3file.read())
    except Exception as err:
        pass


log('[%s] Loaded' % __name__)
