import unittest
from problem7 import setzero


class SetZeroTest(unittest.TestCase):

    def setUp(self):
        self.m = [[1, 2, 3],
                  [4, 5, 6]]
        self.n = [[1, 2, 3],
                  [4, 5, 6]]

    def test_sanity(self):
        setzero(self.m)
        self.assertEquals(self.m, self.n)

        self.m[1][1] = 0
        setzero(self.m)
        expected = [[1, 0, 3],
                    [0, 0, 0]]
        self.assertEquals(self.m, expected)
