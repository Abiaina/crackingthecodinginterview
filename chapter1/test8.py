import unittest
from problem8 import is_rotation


class IsRotationTest(unittest.TestCase):

    def test_sanity(self):
        self.assertEquals(is_rotation("erbottlewat", "waterbottle"), True)
        self.assertEquals(is_rotation("waterbottle", "gogomobile"), False)
