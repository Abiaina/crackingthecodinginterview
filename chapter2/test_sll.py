import unittest
from sll import SinglyLinkedList


class SinglyLinkedListTest(unittest.TestCase):

    def test_empty(self):
        l = []
        sll = SinglyLinkedList(l)
        self.assertEquals(l, list(sll))
        self.assertEquals(len(l), 0)

    def test_sanity(self):
        l = range(10)
        sll = SinglyLinkedList(l)
        self.assertEquals(l, list(sll))
        self.assertEquals(len(l), 10)

    def test_add(self):
        a1 = range(10)
        a2 = range(100, 110)
        sll = SinglyLinkedList(a1) + SinglyLinkedList(a2)
        self.assertEquals(list(sll), a1 + a2)

    def test_append(self):
        a = range(10)
        b = range(11)
        sll = SinglyLinkedList(a)
        self.assertEquals(list(sll), a)
        sll.append(10)
        self.assertEquals(list(sll), b)

    def test_append_empty(self):
        sll = SinglyLinkedList()
        self.assertEquals(list(sll), [])
        sll.append(1)
        self.assertEquals(list(sll), [1])


class TestReverse(unittest.TestCase):

    def test_sanity(self):
        a = range(10)
        sll = SinglyLinkedList(a)
        self.assertEquals(list(sll.reverse()), [x for x in reversed(a)])

    def test_empty(self):
        sll = SinglyLinkedList()
        self.assertEquals(list(sll), [])
