import unittest
import problem3


class TestSolution(unittest.TestCase):

    def test_invalid(self):
        self.assertRaises(ValueError, problem3.solution, 0)
        self.assertRaises(ValueError, problem3.solution, 1)

    def test_valid(self):
        self.assertEquals(problem3.solution(6), (9, 5))
        self.assertEquals(problem3.solution(5), (6, 3))


class TestLarger(unittest.TestCase):

    def test(self):
        self.assertEquals(problem3.larger(124), 143)


class TestSmaller(unittest.TestCase):

    def test(self):
        self.assertRaises(ValueError, problem3.smaller, 0)
        self.assertRaises(ValueError, problem3.smaller, 1)
