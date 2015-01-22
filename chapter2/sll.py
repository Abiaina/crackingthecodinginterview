import unittest


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


class SinglyLinkedListTest(unittest.TestCase):

    def test_empty(self):
        l = []
        sll = SinglyLinkedList(l)
        self.assertEquals(l, list(sll))

    def test_sanity(self):
        l = range(10)
        sll = SinglyLinkedList(l)
        self.assertEquals(l, list(sll))

    def test_add(self):
        a1 = range(10)
        a2 = range(100, 110)
        sll = SinglyLinkedList(a1) + SinglyLinkedList(a2)
        self.assertEquals(list(sll), a1 + a2)

    def test_append(self):
        a = range(10)
        b = range(11)
        sll = SinglyLinkedList(a)
        self.assertEquals(list(sll), a)
        sll.append(10)
        self.assertEquals(list(sll), b)

    def test_append_empty(self):
        sll = SinglyLinkedList()
        self.assertEquals(list(sll), [])
        sll.append(1)
        self.assertEquals(list(sll), [1])
