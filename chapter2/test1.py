import unittest
from sll import SinglyLinkedList
from problem1 import rmdup, rmdup2


class RemoveDuplicatesTest(unittest.TestCase):

    def test_sanity(self):
        self.worker([1, 2, 2, 1, 3], [1, 2, 3], rmdup)

    def test_sanity2(self):
        self.worker([1, 2, 2, 1, 3], [1, 2, 3], rmdup2)

    def worker(self, dup, expected, fn):
        sll = SinglyLinkedList(dup)
        self.assertNotEquals(list(sll), expected)
        self.assertEquals(list(fn(sll)), expected)
