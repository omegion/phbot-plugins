from classes.plugins.online_manager.events.BaseEvent import BaseEvent


class CharacterInfoReceivedEvent(BaseEvent):
    name = "characters.character_info_received"

    def dispatch(self, character_info):
        self.api.dispatch_event(self.name, character_info)
