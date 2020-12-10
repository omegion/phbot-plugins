from classes.plugins.BasePlugin import BasePlugin, exception_handler


class Control(BasePlugin):
    def __init__(self, gui=None):
        """This is a plugin to control the bot from in-game chat."""

        super().__init__(
            plugin_name=self.__class__.__name__,
        )

        self.gui = gui

    @exception_handler
    def setup(self):
        self.initialize()
        self.bot.log('loaded')
