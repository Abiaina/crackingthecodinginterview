#
# Given a circular linked list, implement an algorithm which returns the node
# at the beginning of a loop.
#
import unittest
from sll import SinglyLinkedList


def start_of_loop(sll):
    """Simple implementation using a buffer."""
    seen = set()
    curr = sll.head
    while curr:
        if curr in seen:
            return curr
        seen.add(curr)
        curr = curr.next_
    return None


def start_of_loop2(sll):
    """A "clever" implementation that does not use a buffer."""
    #
    # Use Floyd's cycle finding algorithm
    # (http://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare)
    # to determine if we are stuck in a loop.
    #
    tortoise = sll.head
    hare = sll.head.next_
    if hare:
        hare = hare.next_
    while hare and tortoise and hare != tortoise:
        tortoise = tortoise.next_
        hare = hare.next_
        if hare:
            hare = hare.next_
    if hare is None or tortoise is None:
        return None
    #
    # We are now in a loop. Let's find its size.
    #
    loop_length = 1
    hare = hare.next_
    while hare != tortoise:
        hare = hare.next_
        loop_length += 1
    #
    # Use a leading pointer to find the start of the loop.
    #
    hare = tortoise = sll.head
    for _ in xrange(loop_length):
        hare = hare.next_
    while hare != tortoise:
        hare = hare.next_
        tortoise = tortoise.next_
    return hare


class StartOfLoopTest(unittest.TestCase):

    def setUp(self):
        self.sll = SinglyLinkedList("abcde")
        self.sll.tail.next_ = self.sll.head.next_.next_
        self.start_of_loop = self.sll.tail.next_

        #
        # Technically, our SinglyLinkedList isn't suitable for solving this
        # problem, since it has a tail pointer, and circular lists cannot
        # have a tail.  However, it's "good enough" to demonstrate the
        # solution, since the solution never uses the tail pointer.
        #
        self.sll.tail = None

    def test_no_loop(self):
        self.assertEquals(start_of_loop(SinglyLinkedList("misha")), None)

    def test_loop(self):
        self.assertEquals(start_of_loop(self.sll), self.start_of_loop)

    def test_no_loop_clever(self):
        self.assertEquals(start_of_loop2(SinglyLinkedList("misha")), None)

    def test_loop_clever(self):
        self.assertEquals(start_of_loop2(self.sll), self.start_of_loop)
