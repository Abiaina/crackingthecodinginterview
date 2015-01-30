class Node(object):

    def __init__(self, payload, next_=None):
        self.payload = payload
        self.next_ = next_


class Stack(object):

    def __init__(self, iterable=[]):
        """Create a new stack.
        Optionally, populate it with the items in an iterable.
        The end of the iterable is the top of the stack."""
        self.top = None
        self.numitems = 0
        for payload in iterable:
            self.push(payload)

    def peek(self):
        if not self.top:
            raise ValueError("empty stack")
        return self.top.payload

    def pop(self):
        if not self.top:
            raise ValueError("empty stack")
        payload = self.top.payload
        self.top = self.top.next_
        self.numitems -= 1
        return payload

    def push(self, value):
        self.top = Node(value, self.top)
        self.numitems += 1

    def __repr__(self):
        payloads = []
        curr = self.top
        while curr:
            payloads.append(curr.payload)
            curr = curr.next_
        return "Stack(%s)" % repr(payloads)

    def __len__(self):
        return self.numitems

    def is_empty(self):
        return self.numitems == 0
