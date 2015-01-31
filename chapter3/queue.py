from stack import Node


class Queue(object):

    def __init__(self, iterable=[]):
        """Create a new stack.
        Optionally, populate it with the items in an iterable.
        The end of the iterable is the top of the stack."""
        self.front = self.back = None
        for payload in iterable:
            self.enqueue(payload)

    def enqueue(self, value):
        new_node = Node(value)
        if self.back is None:
            self.front = self.back = new_node
        else:
            self.back.next_ = new_node
            self.back = new_node

    def peek(self):
        if not self.front:
            raise ValueError("empty queue")
        return self.front.payload

    def dequeue(self):
        if not self.front:
            raise ValueError("empty queue")
        result = self.front.payload
        if self.front == self.back:
            self.front = self.back = None
        else:
            self.front = self.front.next_
        return result

    def __repr__(self):
        payloads = []
        curr = self.front
        while curr:
            payloads.append(curr.payload)
            curr = curr.next_
        return "Queue(%s)" % repr(payloads)
