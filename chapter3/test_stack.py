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
        self.assertEquals(len(stack), 4)
        self.assertEquals(stack.pop(), "d")
        self.assertEquals(len(stack), 3)
        self.assertEquals(stack.pop(), "c")
        self.assertEquals(len(stack), 2)
        self.assertEquals(stack.pop(), "b")
        self.assertEquals(len(stack), 1)
        self.assertEquals(stack.pop(), "a")
        self.assertEquals(len(stack), 0)

    def test_peek(self):
        stack = Stack("abcd")
        print repr(stack)
        self.assertEquals(stack.peek(), "d")
        self.assertEquals(stack.peek(), "d")

    def test_push(self):
        stack = Stack()
        stack.push("a")
        self.assertEquals(stack.peek(), "a")
        self.assertEquals(len(stack), 1)
        stack.push("b")
        self.assertEquals(stack.peek(), "b")
        self.assertEquals(len(stack), 2)
