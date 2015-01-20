#
# Implement an algorithm to delete a node in the middle of a singly linked
# list, given access only to that node.
#
# EXAMPLE:
# Input: the node c from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a->b->d->e
#
import unittest
from sll import SinglyLinkedList


def delete_middle(node):
    if node.next_ is None:
        raise ValueError("node is at the end of the list")
    node.payload = node.next_.payload
    node.next_ = node.next_.next_


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
