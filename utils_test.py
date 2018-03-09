import unittest

import utils


class UtilsTest(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(utils.convert('2018-03-09 17:06:30.129420+00:00'), 1520629590129.42)

    def test_current_epoch(self):
        print(utils.current_epoch())
