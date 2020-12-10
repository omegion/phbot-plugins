import QtBind

from classes.plugins.Downloader import Downloader

gui = QtBind.init(__name__, Downloader.__name__)

plugin = Downloader(
    gui=gui,
)

plugin.setup()


def save():
    plugin.save()
