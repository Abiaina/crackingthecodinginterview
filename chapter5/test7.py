import unittest
import problem7


class TestArray(unittest.TestCase):

    def test(self):
        A = problem7.Array(10, 5)
        self.assertEquals(A.access(0, 0), 0)
        self.assertEquals(A.access(0, 1), 0)
        self.assertEquals(A.access(0, 2), 0)
        self.assertEquals(A.access(0, 3), 0)
        self.assertEquals(A.access(0, 4), 0)
        self.assertEquals(A.access(0, 5), 0)
        self.assertEquals(A.access(0, 6), 0)
        self.assertEquals(A.access(0, 7), 0)
        self.assertEquals(A.access(0, 8), 0)

        self.assertEquals(A.access(3, 0), 1)
        self.assertEquals(A.access(3, 1), 1)
        self.assertEquals(A.access(3, 2), 0)
        self.assertEquals(A.access(3, 3), 0)
        self.assertEquals(A.access(3, 4), 0)
        self.assertEquals(A.access(3, 5), 0)
        self.assertEquals(A.access(3, 6), 0)
        self.assertEquals(A.access(3, 7), 0)
        self.assertEquals(A.access(3, 8), 0)

        self.assertEquals(A.access(9 - 1, 0), 1)
        self.assertEquals(A.access(9 - 1, 1), 0)
        self.assertEquals(A.access(9 - 1, 2), 0)
        self.assertEquals(A.access(9 - 1, 3), 1)
        self.assertEquals(A.access(9 - 1, 4), 0)
        self.assertEquals(A.access(9 - 1, 5), 0)
        self.assertEquals(A.access(9 - 1, 6), 0)
        self.assertEquals(A.access(9 - 1, 7), 0)
        self.assertEquals(A.access(9 - 1, 8), 0)


class TestSolve(unittest.TestCase):

    def test(self):
        A = problem7.Array(10, 5)
        self.assertEquals(problem7.solve(A), 5)
