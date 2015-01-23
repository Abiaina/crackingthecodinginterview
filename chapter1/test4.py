import unittest
from problem4 import escape_spaces


class EscapeSpacesTest(unittest.TestCase):

    def test_sanity(self):
        self.assertEquals(escape_spaces("test"), "test")
        self.assertEquals(escape_spaces("test this"), "test%20this")
        self.assertEquals(escape_spaces("this is a test"),
                          "this%20is%20a%20test")
        self.assertEquals(escape_spaces("Mr John Smith"), "Mr%20John%20Smith")
