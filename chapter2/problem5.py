#
# You have two numbers represented by a linked list, where each node contains
# a single digit.  The digits are stored in reverse order such that the 1's
# digit is at the head of the list.  Write a function that adds the two
# numbers and returns the sum as a linked list.
#
# FOLLOW UP: suppose the digits are stored in forward order.  Repeat the above
# problem.
#
import unittest
from sll import SinglyLinkedList, SinglyLinkedListNode


def reverse(sll):
    """Returns a reversed version of a linked list."""
    result = SinglyLinkedList()
    for value in sll:
        result.head = SinglyLinkedListNode(value, result.head)
    return result


def add(left, right, msd=False):
    """Set msd to True if left and right are in "most significant digit
    first" order.  The result will be in the same order as the input."""
    if msd:
        left = reverse(left)
        right = reverse(right)
    result = SinglyLinkedList()
    carry = 0
    a = left.head
    b = right.head
    while a and b:
        c = a.payload + b.payload
        result.append(carry + c % 10)
        carry = c / 10
        a = a.next_
        b = b.next_
    while a:
        result.append(a.payload)
        a = a.next_
    while b:
        result.append(b.payload)
        b = b.next_
    if msd:
        return reverse(result)
    return result


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


class TestReverse(unittest.TestCase):

    def test_sanity(self):
        a = range(10)
        sll = SinglyLinkedList(a)
        self.assertEquals(list(reverse(sll)), [x for x in reversed(a)])

    def test_empty(self):
        sll = SinglyLinkedList()
        self.assertEquals(list(sll), [])
