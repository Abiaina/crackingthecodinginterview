import unittest


class SinglyLinkedListNode(object):

    def __init__(self, payload, next_=None):
        self.payload = payload
        self.next_ = next_


class SinglyLinkedList(object):

    def __init__(self, elements=[]):
        self.head = None
        for payload in reversed(elements):
            self.head = SinglyLinkedListNode(payload, self.head)

    def __iter__(self):
        current = self.head
        while current:
            yield current.payload
            current = current.next_

    def __repr__(self):
        return "SinglyLinkedList(%s)" % str(list(self))


class SinglyLinkedListTest(unittest.TestCase):

    def test_empty(self):
        l = []
        sll = SinglyLinkedList(l)
        self.assertEquals(l, list(sll))

    def test_sanity(self):
        l = range(10)
        sll = SinglyLinkedList(l)
        self.assertEquals(l, list(sll))
