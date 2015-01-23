import unittest
from problem1 import is_unique, is_unique2


class IsUniqueTest(unittest.TestCase):

    def test_sanity(self):
        self.assertEquals(is_unique("fobar"), True)
        self.assertEquals(is_unique("misha"), True)

        self.assertEquals(is_unique("foobar"), False)
        self.assertEquals(is_unique("mikhail"), False)

    def test_sanity2(self):
        self.assertEquals(is_unique2("fobar"), True)
        self.assertEquals(is_unique2("misha"), True)

        self.assertEquals(is_unique2("foobar"), False)
        self.assertEquals(is_unique2("mikhail"), False)
