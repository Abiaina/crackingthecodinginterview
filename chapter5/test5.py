import unittest
import problem5


class TestHamming(unittest.TestCase):

    def test_example(self):
        self.assertEquals(problem5.hamming(31, 14), 2)
