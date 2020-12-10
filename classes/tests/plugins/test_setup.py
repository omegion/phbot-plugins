import unittest

from setup import Setup


class TestPluginSetup(unittest.TestCase):
    def test(self):
        p = Setup()
        p.get_latest_version()
