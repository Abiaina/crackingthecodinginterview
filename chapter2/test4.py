import unittest
from sll import SinglyLinkedList
from problem4 import partition


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
