import unittest
from sll import SinglyLinkedList
from problem5 import add


class TestAdd(unittest.TestCase):

    def test_lsd(self):
        a = SinglyLinkedList([7, 1, 6])
        b = SinglyLinkedList([5, 9, 2])
        c = [2, 1, 9]
        self.assertEquals(list(add(a, b)), c)

    def test_msd(self):
        a = SinglyLinkedList([6, 1, 7])
        b = SinglyLinkedList([2, 9, 5])
        c = [9, 1, 2]
        self.assertEquals(list(add(a, b, True)), c)

    def test_diff_lsd(self):
        a = SinglyLinkedList([1, 2, 3])
        b = SinglyLinkedList([2])
        c = [3, 2, 3]
        self.assertEquals(list(add(a, b)), c)

    def test_diff_msd(self):
        a = SinglyLinkedList([1, 2, 3])
        b = SinglyLinkedList([2])
        c = [1, 2, 5]
        self.assertEquals(list(add(a, b, True)), c)
