import unittest

import api


class ApiTest(unittest.TestCase):
    def test_startup(self):
        print(api.startup())

    def test_parameters(self):
        print(api.parameters())
