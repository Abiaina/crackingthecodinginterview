#
# Implement a function to check if a linked list is a palindrome.
#


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
