import urllib

from classes.plugins.BasePlugin import BasePlugin


class Downloader(BasePlugin):
    def __init__(self, gui=None):
        """This is a helper for force chars."""

        super().__init__(
            plugin_name=self.__class__.__name__,
        )

        self.gui = gui

    def save(self):
        mp3file = urllib.urlopen("http://www.example.com/songs/mp3.mp3")
        with open('test.mp3', 'wb') as output:
            output.write(mp3file.read())

    def setup(self):
        self.initialize()

        active_skill = self.config.get('active_skill')
        party_member_hp = self.config.get('party_member_hp')

        self.bot.qt.createButton(self.gui, 'save', 'save', 95, 250)

        self.bot.log('loaded')
