import unittest
import problem6


class TestSwap(unittest.TestCase):

    def test(self):
        self.assertEquals(problem6.swap(0), 0)
        self.assertEquals(problem6.swap(1), 2)
        self.assertEquals(problem6.swap(2), 1)
        self.assertEquals(problem6.swap(3), 3)
        self.assertEquals(problem6.swap(4), 8)
        self.assertEquals(problem6.swap(5), 10)
        self.assertEquals(problem6.swap(6), 9)
        self.assertEquals(problem6.swap(7), 11)
        self.assertEquals(problem6.swap(8), 4)
        self.assertEquals(problem6.swap(9), 6)
        self.assertEquals(problem6.swap(10), 5)
        self.assertEquals(problem6.swap(11), 7)
        self.assertEquals(problem6.swap(12), 12)
        self.assertEquals(problem6.swap(13), 14)
        self.assertEquals(problem6.swap(14), 13)
        self.assertEquals(problem6.swap(15), 15)
