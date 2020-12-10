from classes.plugins.BasePlugin import BasePlugin, exception_handler
from classes.plugins.online_manager.events.CharacterInfoReceivedEvent import CharacterInfoReceivedEvent

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMjM3MTI4NDQzLCJqdGkiOiIyYzg2ZDQ5YzFiYmI0NzUyYTA5NjIzN2JmMzMwYzU3YSIsInVzZXJfaWQiOjF9.qQIkKflsNr1ppf99YE_yKa27f-LZcVAYuDZLbUmmuu8'


class OnlineManager(BasePlugin):
    def __init__(self, gui=None):
        """This is a plugin for online management"""

        super().__init__(
            plugin_name=self.__class__.__name__,
            token=TOKEN
        )

        self.gui = gui

    def send_char_info(self):
        character_info = self.bot.get_character_data()
        character_info['is_botting'] = self._is_botting()
        character_info['is_clientless'] = self._is_clientless()
        character_info['bot_version'] = self.bot.get_version()
        character_info['profile_name'] = self.bot.get_profile()
        character_info['drops'] = self._get_drops_count()

        event = CharacterInfoReceivedEvent(self.api)
        event.dispatch(character_info)

    def execute_queued_tasks(self):
        self.api.execute_queued_tasks()

    @exception_handler
    def event_loop(self):
        pass

    @exception_handler
    def setup(self):
        self.initialize()

        self.bot.qt.createButton(self.gui, 'send_char_info', 'send_char_info', 10, 250)
        self.bot.qt.createButton(self.gui, 'execute_queued_tasks', 'execute_queued_tasks', 10, 95)

        self.bot.log('loaded')

    def _is_botting(self):
        return self.bot.get_status() == 'botting'

    def _is_clientless(self):
        client_status = self.bot.get_client()
        return not client_status.get('running', False)

    def _get_drops_count(self):
        drops = self.bot.get_drops()
        if drops:
            return len(drops)
        return 0
