import unittest
from problem5 import compress


class CompressTest(unittest.TestCase):

    def test_sanity(self):
        self.assertEquals(compress("aabcccccaaa"), "a2b1c5a3")
        self.assertEquals(compress("unique"), "unique")
