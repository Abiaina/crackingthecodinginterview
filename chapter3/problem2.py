#
# How would you design a stack which, in addition to push and pop, also has a
# function min that returns the minimum element?  Push, pop and min should all
# operate in O(1) time.
#
from stack import Stack


class StackWithMin(object):

    def __init__(self, iterable=[]):
        self.actual_values = Stack()
        self.minimum_values = Stack()
        for value in iterable:
            self.push(value)

    def push(self, value):
        self.actual_values.push(value)
        try:
            old_minimum = self.minimum_values.peek()
        except ValueError:
            old_minimum = value
        self.minimum_values.push(min(value, old_minimum))

    def peek(self):
        return self.actual_values.peek()

    def minimum(self):
        return self.minimum_values.peek()

    def pop(self):
        self.minimum_values.pop()
        return self.actual_values.pop()
