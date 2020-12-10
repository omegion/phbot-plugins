import QtBind
from phBot import *

from classes.plugins.online_manager.OnlineManager import OnlineManager

gui = QtBind.init(__name__, OnlineManager.__name__)

plugin = OnlineManager(
    gui=gui,
)

plugin.setup()


def send_char_info():
    plugin.send_char_info()


def execute_queued_tasks():
    plugin.execute_queued_tasks()
