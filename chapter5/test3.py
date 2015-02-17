import unittest
import problem3


class TestSolution(unittest.TestCase):

    def test_invalid(self):
        self.assertRaises(ValueError, problem3.solution, 0)
        self.assertRaises(ValueError, problem3.solution, 1)

    def test_valid(self):
        self.assertEquals(problem3.solution(6), (12, 5))
        self.assertEquals(problem3.solution(5), (6, 3))
