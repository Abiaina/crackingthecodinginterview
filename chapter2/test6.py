import unittest
from sll import SinglyLinkedList
from problem6 import start_of_loop, start_of_loop2


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
