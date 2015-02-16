import unittest
import problem2


class TestBinaryRepr(unittest.TestCase):

    def test_sanity(self):
        self.assertEquals(problem2.binary_repr(0.0), "0")

        self.assertEquals(problem2.binary_repr(0.5), "0.1")
        self.assertEquals(problem2.binary_repr(0.25), "0.01")
        self.assertEquals(problem2.binary_repr(0.125), "0.001")

        self.assertEquals(problem2.binary_repr(0.75), "0.11")

        self.assertEquals(problem2.binary_repr(0.1), "ERROR")
