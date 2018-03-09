import unittest

from logger import Logger


class LoggerTest(unittest.TestCase):
    def test_log(self):
        log = Logger(print_val=True)
        log.log('sdaffsdf1')
        log.log('sdaffsdf2')
        log.log('sdaffsdf3')
