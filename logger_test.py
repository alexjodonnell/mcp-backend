import unittest

from logger import Logger


class LoggerTest(unittest.TestCase):
    def test_log(self):
        log = Logger()
        log.log('sdaffsdf')
        log.log('sdaffsdf')
        log.log('sdaffsdf')
