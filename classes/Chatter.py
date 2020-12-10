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
    def get_chatter(self) -> FakeChat:
        try:
            import phBotChat
            return phBotChat
        except ImportError:
            return FakeChat()
