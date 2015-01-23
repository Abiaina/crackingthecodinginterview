class SinglyLinkedListNode(object):

    def __init__(self, payload, next_=None):
        self.payload = payload
        self.next_ = next_


class SinglyLinkedList(object):

    def __init__(self, elements=[]):
        self.head = None
        self.tail = None
        for payload in reversed(elements):
            self.head = SinglyLinkedListNode(payload, self.head)
            if self.tail is None:
                self.tail = self.head

    def __add__(self, other):
        """Concatenate this list with another singly linked list."""
        if not isinstance(other, SinglyLinkedList):
            raise ValueError("other must be a SinglyLinkedList")
        if self.head is None:
            self.head = other.head
        else:
            self.tail.next_ = other.head
            self.tail = other.tail
        return self

    def __iter__(self):
        current = self.head
        while current:
            yield current.payload
            current = current.next_

    def __len__(self):
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next_
        return length

    def __repr__(self):
        return "SinglyLinkedList(%s)" % str(list(self))

    def append(self, value):
        """Append a value to the end of this list."""
        node = SinglyLinkedListNode(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next_ = node
            self.tail = self.tail.next_

    def reverse(self):
        """Returns a reversed copy of this linked list."""
        result = SinglyLinkedList()
        for value in self:
            result.head = SinglyLinkedListNode(value, result.head)
        return result
