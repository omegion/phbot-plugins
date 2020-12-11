import QtBind
from phBot import log

try:
    from classes.plugins.ForceTools import ForceTools

    gui = QtBind.init(__name__, ForceTools.__name__)

    plugin = ForceTools(
        gui=gui,
    )

    plugin.setup()


    def joined_game():
        plugin.joined_game()


    def save():
        plugin.save()

except Exception:
    log('Classes are missing, please install it with setup plugin.')
