import unittest
from problem2 import reverse


class ReverseTest(unittest.TestCase):

    def test_sanity(self):
        self.assertEquals(reverse("misha"), "ahsim")
        self.assertEquals(reverse("mikhail"), "liahkim")
        self.assertEquals(reverse("foob"), "boof")
        self.assertEquals(reverse("radar"), "radar")
