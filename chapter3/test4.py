import unittest
from problem4 import Tower, Hanoi


class TowerTest(unittest.TestCase):

    def test_constructor(self):
        t = Tower([3, 2, 1])
        self.assertEquals(t.pop(), 1)
        self.assertEquals(t.pop(), 2)
        self.assertEquals(t.pop(), 3)

    def test_bad_constructor(self):
        self.assertRaises(ValueError, Tower, [1, 2, 3])

    def test_push(self):
        t = Tower()
        t.push(1)
        self.assertEquals(t.peek(), 1)
        self.assertRaises(ValueError, t.push, 2)


class HanoiTest(unittest.TestCase):

    def setUp(self):
        self.h = Hanoi([5, 4, 3, 2, 1])

    def test_constructor(self):
        self.assertEquals(len(self.h.towers[0]), 5)
        self.assertEquals(len(self.h.towers[1]), 0)
        self.assertEquals(len(self.h.towers[2]), 0)

        self.assertEquals(self.h.towers[0].pop(), 1)
        self.assertEquals(self.h.towers[0].pop(), 2)
        self.assertEquals(self.h.towers[0].pop(), 3)
        self.assertEquals(self.h.towers[0].pop(), 4)
        self.assertEquals(self.h.towers[0].pop(), 5)

    def test_solve(self):
        self.h.solve()

        self.assertEquals(len(self.h.towers[0]), 0)
        self.assertEquals(len(self.h.towers[1]), 0)
        self.assertEquals(len(self.h.towers[2]), 5)

        self.assertEquals(self.h.towers[2].pop(), 1)
        self.assertEquals(self.h.towers[2].pop(), 2)
        self.assertEquals(self.h.towers[2].pop(), 3)
        self.assertEquals(self.h.towers[2].pop(), 4)
        self.assertEquals(self.h.towers[2].pop(), 5)
