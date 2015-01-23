import unittest
from sll import SinglyLinkedList
from problem2 import kth_to_last


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
