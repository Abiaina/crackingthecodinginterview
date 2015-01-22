#
# Write code to partition a linked list around a value x, such that all nodes
# less than x come before all nodes greater than or equal to x.
#
import unittest
from sll import SinglyLinkedList


def partition(sll, x):
    lt = SinglyLinkedList()
    geq = SinglyLinkedList()
    for value in sll:
        if value < x:
            lt.append(value)
        else:
            geq.append(value)
    return lt + geq


class TestPartition(unittest.TestCase):

    def test_empty(self):
        sll = SinglyLinkedList()
        self.assertEquals(list(sll), [])
        sll = partition(sll, 10)
        self.assertEquals(list(sll), [])

    def test_sanity(self):
        sll = SinglyLinkedList([1, 2, 1, 3, 2, 0])
        sll = partition(sll, 2)
        self.assertEquals(list(sll), [1, 1, 0, 2, 3, 2])

    def test_sanity2(self):
        sll = SinglyLinkedList(range(50, 60) + range(10))
        sll = partition(sll, 10)
        self.assertEquals(list(sll), range(10) + range(50, 60))
