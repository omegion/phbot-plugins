import QtBind
from phBot import *

gui = QtBind.init(__name__, 'Reload Config')

QtBind.createLabel(gui,
                   'Welcome to the Reload Config',
                   10, 10)

reload_button = QtBind.createButton(gui, 'generate', 'Generate', 10, 30)


def generate():
    set_profile(get_profile())
    log('Profile reloaded.')


log('[%s] Loaded' % __name__)
