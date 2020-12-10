import QtBind
from phBot import *

from classes.plugins.AutoTrade import AutoTrade

gui = QtBind.init(__name__, AutoTrade.__name__)

plugin = AutoTrade(
    gui=gui,
)

plugin.setup()


# Button Methods
def check_pouch():
    plugin.check_pouch()

    # plugin.bot.log(plugin.bot.get_character_data())
    # plugin.bot.log(plugin.bot.get_status())
    # plugin.bot.log(plugin.bot.get_drops())
    # plugin.bot.log(plugin.bot.get_client())
    plugin.bot.log(plugin.bot.get_version())
    # plugin.bot.log(plugin.char.__dict__)


def start_trade():
    plugin.start_trade()


# Native Methods
def joined_game():
    plugin.joined_game()


# Script Commands
def stop_trade(*args):
    plugin.stop_trade()

    return 5000
