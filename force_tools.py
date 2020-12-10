import QtBind

from classes.plugins.ForceTools import ForceTools

gui = QtBind.init(__name__, ForceTools.__name__)

plugin = ForceTools(
    gui=gui,
)

plugin.setup()


def save():
    plugin.save()
