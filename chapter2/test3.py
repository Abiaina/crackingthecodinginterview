import unittest
from sll import SinglyLinkedList
from problem3 import delete_middle


class DeleteMiddleTest(unittest.TestCase):

    def setUp(self):
        self.sll = SinglyLinkedList("abcde")

    def test_last(self):
        last = self.sll.head
        while last.next_ is not None:
            last = last.next_
        self.assertRaises(ValueError, delete_middle, last)

    def test_c(self):
        c = self.sll.head
        while c.payload != "c":
            c = c.next_
        delete_middle(c)
        self.assertEquals(list(self.sll), list("abde"))
