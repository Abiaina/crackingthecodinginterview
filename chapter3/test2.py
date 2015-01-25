import unittest
from problem2 import StackWithMin


class StackTest(unittest.TestCase):

    def test_empty(self):
        stack = StackWithMin([])
        self.assertRaises(ValueError, stack.peek)
        self.assertRaises(ValueError, stack.pop)

    def test_pop(self):
        stack = StackWithMin("abcd")
        print repr(stack)
        self.assertEquals(stack.minimum(), "a")
        self.assertEquals(stack.pop(), "d")
        self.assertEquals(stack.minimum(), "a")
        self.assertEquals(stack.pop(), "c")
        self.assertEquals(stack.minimum(), "a")
        self.assertEquals(stack.pop(), "b")
        self.assertEquals(stack.minimum(), "a")
        self.assertEquals(stack.pop(), "a")

    def test_peek(self):
        stack = StackWithMin("abcd")
        print repr(stack)
        self.assertEquals(stack.peek(), "d")
        self.assertEquals(stack.peek(), "d")

    def test_push(self):
        stack = StackWithMin()
        stack.push("b")
        self.assertEquals(stack.peek(), "b")
        self.assertEquals(stack.minimum(), "b")
        stack.push("a")
        self.assertEquals(stack.peek(), "a")
        self.assertEquals(stack.minimum(), "a")
