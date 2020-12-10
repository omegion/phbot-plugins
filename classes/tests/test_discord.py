import unittest

from classes.Discord import DiscordMessage


class TestPluginSetup(unittest.TestCase):
    def test(self):
        m = DiscordMessage("hey", "there")
        m.send()
