#
# You have two numbers represented by a linked list, where each node contains
# a single digit.  The digits are stored in reverse order such that the 1's
# digit is at the head of the list.  Write a function that adds the two
# numbers and returns the sum as a linked list.
#
# FOLLOW UP: suppose the digits are stored in forward order.  Repeat the above
# problem.
#
from sll import SinglyLinkedList


def add(left, right, msd=False):
    """Set msd to True if left and right are in "most significant digit
    first" order.  The result will be in the same order as the input."""
    if msd:
        left = left.reverse()
        right = right.reverse()
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
        return result.reverse()
    return result
