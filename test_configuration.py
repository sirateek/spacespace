import unittest
from consts import *


class TestConfiguration(unittest.TestCase):
    def test_deathable_config(self):
        self.assertEqual(IS_DEATHABLE, True)
