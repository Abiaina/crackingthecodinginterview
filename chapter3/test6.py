import unittest

from problem6 import sort_stack
from stack import Stack


class TestSortStack(unittest.TestCase):

    def test_empty(self):
        s = Stack()
        self.assertEquals(s.is_empty(), True)
        sort_stack(s)
        self.assertEquals(s.is_empty(), True)

    def test_sort(self):
        s = Stack([5, 8, 2, 10, 4, 11])
        sort_stack(s)

        self.assertEquals(s.pop(), 11)
        self.assertEquals(s.pop(), 10)
        self.assertEquals(s.pop(), 8)
        self.assertEquals(s.pop(), 5)
        self.assertEquals(s.pop(), 4)
        self.assertEquals(s.pop(), 2)
