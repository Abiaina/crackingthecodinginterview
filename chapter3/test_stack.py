import unittest
from stack import Stack


class StackTest(unittest.TestCase):

    def test_empty(self):
        stack = Stack([])
        self.assertRaises(ValueError, stack.peek)
        self.assertRaises(ValueError, stack.pop)

    def test_pop(self):
        stack = Stack("abcd")
        print repr(stack)
        self.assertEquals(stack.pop(), "d")
        self.assertEquals(stack.pop(), "c")
        self.assertEquals(stack.pop(), "b")
        self.assertEquals(stack.pop(), "a")

    def test_peek(self):
        stack = Stack("abcd")
        print repr(stack)
        self.assertEquals(stack.peek(), "d")
        self.assertEquals(stack.peek(), "d")
