import QtBind
from phBot import log

try:
    from classes.plugins.Control import Control

    gui = QtBind.init(__name__, Control.__name__)

    plugin = Control(
        gui=gui,
    )

    plugin.setup()


    def handle_chat(t, player, msg):
        plugin.handle_chat(t, player, msg)


    def joined_game():
        plugin.joined_game()


    def get_position_button_action():
        plugin.get_position()


    def add_leader_button_action():
        plugin.add_leader()


    def remove_leader_button_action():
        plugin.remove_leader()


except ImportError:
    log('Classes are missing, please install it with setup plugin.')
