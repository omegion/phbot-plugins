import unittest

from classes.plugins.AutoTrade import AutoTrade


class TestPluginSetup(unittest.TestCase):
    def test(self):
        plugin = AutoTrade()

        db = plugin.bot.get_db()

        holder = 1
