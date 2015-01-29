#
# Implement a MyQueue class that implements a queue using two stacks.
#
from stack import Stack


class MyQueue(object):

    def __init__(self):
        self.stack = Stack()
        self.buf = Stack()
        self.reversed_stack = False

    def enqueue(self, value):
        if self.reversed_stack:
            self.__reverse_stack()
        self.stack.push(value)

    def dequeue(self):
        if not self.reversed_stack:
            self.__reverse_stack()
        return self.stack.pop()

    def __reverse_stack(self):
        assert len(self.buf) == 0
        while len(self.stack):
            self.buf.push(self.stack.pop())
        self.buf, self.stack = self.stack, self.buf
        self.reversed_stack = not self.reversed_stack
