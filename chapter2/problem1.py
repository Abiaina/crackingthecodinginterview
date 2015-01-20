#
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: how would you solve this problem if a temporary buffer was not
# allowed?
#
import unittest
from sll import SinglyLinkedList


def rmdup(sll):
    """Remove duplicates by keeping track of seen elements in a buffer."""
    seen = set()
    prev = None
    current = sll.head
    while current:
        if current.payload in seen:
            prev.next_ = current.next_
            current = current.next_
        else:
            seen.add(current.payload)
            prev = current
            current = current.next_
    return sll  # for chaining


def rmdup2(sll):
    """Remove duplicates without using an additional buffer."""
    start = sll.head
    while start:
        node = start
        while node and node.next_:
            if node.next_.payload == start.payload:
                node.next_ = node.next_.next_
            node = node.next_
        start = start.next_
    return sll
        

class RemoveDuplicatesTest(unittest.TestCase):

    def test_sanity(self):
        self.worker([1, 2, 2, 1, 3], [1, 2, 3], rmdup)

    def test_sanity2(self):
        self.worker([1, 2, 2, 1, 3], [1, 2, 3], rmdup2)

    def worker(self, dup, expected, fn):
        sll = SinglyLinkedList(dup)
        self.assertNotEquals(list(sll), expected)
        self.assertEquals(list(fn(sll)), expected)
