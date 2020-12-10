import QtBind

from classes.plugins.ForceTools import ForceTools

gui = QtBind.init(__name__, ForceTools.__name__)

plugin = ForceTools(
    gui=gui,
)

try:
    plugin.setup()


    def save():
        plugin.save()
except Exception as e:
    plugin.bot.exception(e)
