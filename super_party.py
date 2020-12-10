import QtBind

from classes.plugins.SuperParty import SuperParty

TOKEN = "Nzc4MzM3NTA1NjY1NDgyODIy.X7QhSg.9ac1cs01XuysMMEPwYfdwo2tKw0"

gui = QtBind.init(__name__, SuperParty.__name__)

plugin = SuperParty(
    gui=gui,
)

plugin.setup()

thread = None


def handle_event(t, data):
    plugin.handle_event(t, data)


def save_config(*args):
    plugin.save_config()

# def on_exit():
#     try:
#         thread.loop.stop()
#     except Exception as e:
#         plugin.bot.exception(e)
#
#     plugin.bot.log_to_file('Plugin exited.')
#
#
# import atexit
#
# atexit.register(on_exit)
