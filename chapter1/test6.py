import unittest
from problem6 import rotate_clockwise, rotate_anticlockwise


class RotateTest(unittest.TestCase):

    def setUp(self):
        self.m = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        self.n = [[7, 4, 1],
                  [8, 5, 2],
                  [9, 6, 3]]

    def test_clockwise(self):
        self.assertEquals(rotate_clockwise(self.m), self.n)

    def test_rotate_anticlockwise(self):
        self.assertEquals(rotate_anticlockwise(self.n), self.m)
