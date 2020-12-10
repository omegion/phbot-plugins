class FakeChat(object):
    def All(self, message):
        print(message)

    def Private(self, message, player):
        print(message)

    def Party(self, message):
        print(message)

    def Guild(self, message):
        print(message)

    def Union(self, message):
        print(message)

    def Note(self, message, player):
        print(message)

    def Stall(self, message):
        print(message)

    def Global(self, message):
        print(message)


class Chatter(object):
    def __init__(self):
        self.chat = self.get_chatter()

    def get_chatter(self):
        try:
            import phBotChat
            return phBotChat
        except ImportError:
            return FakeChat()
