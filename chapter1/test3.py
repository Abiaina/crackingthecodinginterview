import unittest
from problem3 import is_permutation


class IsPermutationTest(unittest.TestCase):

    def test_sanity(self):
        self.assertEquals(is_permutation("misha", "ahsim"), True)
        self.assertEquals(is_permutation("foobar", "raboof"), True)
        self.assertEquals(is_permutation("radar", "radar"), True)
