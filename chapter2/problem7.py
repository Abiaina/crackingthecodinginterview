#
# Implement a function to check if a linked list is a palindrome.
#
import unittest
from sll import SinglyLinkedList


def is_palindrome(sll):
    rev = sll.reverse()  # or use a doubly-linked list
    left = sll.head
    right = rev.head
    for _ in xrange(len(sll) / 2):
        if left.payload != right.payload:
            return False
        left = left.next_
        right = right.next_
    return True


class IsPalindromeTest(unittest.TestCase):

    def test_empty(self):
        self.assertEquals(is_palindrome(SinglyLinkedList("")), True)

    def test_sanity(self):
        self.assertEquals(is_palindrome(SinglyLinkedList("x")), True)
        self.assertEquals(is_palindrome(SinglyLinkedList("radar")), True)
        self.assertEquals(is_palindrome(SinglyLinkedList("sonar")), False)
