import unittest
from sll import SinglyLinkedList
from problem7 import is_palindrome


class IsPalindromeTest(unittest.TestCase):

    def test_empty(self):
        self.assertEquals(is_palindrome(SinglyLinkedList("")), True)

    def test_sanity(self):
        self.assertEquals(is_palindrome(SinglyLinkedList("x")), True)
        self.assertEquals(is_palindrome(SinglyLinkedList("radar")), True)
        self.assertEquals(is_palindrome(SinglyLinkedList("sonar")), False)
