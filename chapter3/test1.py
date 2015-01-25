import unittest
from problem1 import TripleStack


class TripleStackTest(unittest.TestCase):

    def setUp(self):
        self.stack = TripleStack(3)

    def test_sanity(self):
        self.stack.push(0, "homer")
        self.assertEquals(self.stack.peek(0), "homer")

        self.stack.push(1, "red")
        self.assertEquals(self.stack.peek(1), "red")

        self.stack.push(2, "ramen")
        self.assertEquals(self.stack.peek(2), "ramen")

        self.assertEquals(self.stack.pop(0), "homer")
        self.assertEquals(self.stack.pop(1), "red")
        self.assertEquals(self.stack.pop(2), "ramen")

    def test_full(self):
        self.stack.push(1, "red")
        self.stack.push(1, "green")
        self.stack.push(1, "blue")
        self.assertEquals(self.stack.peek(1), "blue")

        self.assertRaises(ValueError, self.stack.push, 1, "cyan")
        self.assertEquals(self.stack.peek(1), "blue")

        self.stack.push(0, "homer")
        self.stack.push(0, "marge")
        self.stack.push(0, "bart")

        self.assertRaises(ValueError, self.stack.push, 0, "lisa")
        self.assertEquals(self.stack.peek(0), "bart")

    def test_empty(self):
        self.assertRaises(ValueError, self.stack.peek, 0)
        self.assertRaises(ValueError, self.stack.pop, 0)
        self.assertRaises(ValueError, self.stack.peek, 1)
        self.assertRaises(ValueError, self.stack.pop, 1)
        self.assertRaises(ValueError, self.stack.peek, 2)
        self.assertRaises(ValueError, self.stack.pop, 2)
