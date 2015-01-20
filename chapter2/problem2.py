#
# Implement an algorithm to find the kth to last element of a linked list
#
import unittest
from sll import SinglyLinkedList


def kth_to_last(sll, k):
    if k <= 0:
        raise ValueError("k must be positive")

    first = second = sll.head
    for _ in xrange(k - 1):
        if first is None:
            raise ValueError("list is too short")
        first = first.next_

    if first is None:
        raise ValueError("list is too short")

    while first.next_ is not None:
        first = first.next_
        second = second.next_
    return second.payload


class KthToLastTest(unittest.TestCase):

    def setUp(self):
        self.empty = SinglyLinkedList()
        self.sll = SinglyLinkedList([1, 2, 3])

    def test_empty(self):
        self.assertRaises(ValueError, kth_to_last, self.empty, 1)

    def test_too_short(self):
        self.assertRaises(ValueError, kth_to_last, self.sll, 4)

    def test_sanity(self):
        self.assertEquals(kth_to_last(self.sll, 1), 3)

    def test_sanity2(self):
        self.assertEquals(kth_to_last(self.sll, 2), 2)

    def test_sanity3(self):
        self.assertEquals(kth_to_last(self.sll, 1), 3)

    def test_bad_input(self):
        self.assertRaises(ValueError, kth_to_last, self.sll, 0)
