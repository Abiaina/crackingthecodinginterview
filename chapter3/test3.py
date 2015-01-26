import unittest
from problem3 import SetOfStacks


class SetOfStacksTest(unittest.TestCase):

    def test_empty(self):
        stack = SetOfStacks()
        self.assertRaises(ValueError, stack.peek)
        self.assertRaises(ValueError, stack.pop)

    def test_pop(self):
        stack = SetOfStacks()
        for x in "abcd":
            stack.push(x)
        self.assertEquals(stack.pop(), "d")
        self.assertEquals(stack.pop(), "c")
        self.assertEquals(stack.pop(), "b")
        self.assertEquals(stack.pop(), "a")

    def test_peek(self):
        stack = SetOfStacks()
        for x in "abcd":
            stack.push(x)
        self.assertEquals(stack.peek(), "d")
        self.assertEquals(stack.peek(), "d")

    def test_push(self):
        stack = SetOfStacks()
        stack.push("a")
        self.assertEquals(stack.peek(), "a")
        self.assertEquals(len(stack.substacks), 1)
        stack.push("b")
        self.assertEquals(stack.peek(), "b")
        self.assertEquals(len(stack.substacks), 1)
        stack.push("c")
        self.assertEquals(stack.peek(), "c")
        self.assertEquals(len(stack.substacks), 1)
        stack.push("d")
        self.assertEquals(stack.peek(), "d")
        self.assertEquals(len(stack.substacks), 2)

    def test_pop_at(self):
        stack = SetOfStacks()
        for x in "abcd":
            stack.push(x)
        self.assertEquals(stack.pop_at(0), "c")
        self.assertEquals(len(stack.substacks), 2)
        self.assertEquals(stack.pop_at(0), "b")
        self.assertEquals(len(stack.substacks), 2)
        self.assertEquals(stack.pop_at(0), "a")
        self.assertEquals(len(stack.substacks), 1)
        self.assertEquals(stack.pop_at(0), "d")
        self.assertEquals(len(stack.substacks), 1)
        self.assertRaises(ValueError, stack.pop)
