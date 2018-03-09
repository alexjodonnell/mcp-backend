import unittest

import api


class ApiTest(unittest.TestCase):
    def test_startup(self):
        print(api.startup())
