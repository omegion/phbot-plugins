from sys import exit

import QtBind

try:
    from classes.plugins.Control import Control
except ImportError:
    print('Classes are missing, please install it with setup plugin.')

    exit(0)

gui = QtBind.init(__name__, Control.__name__)

plugin = Control(
    gui=gui,
)

plugin.setup()
