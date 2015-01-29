import unittest
from problem5 import MyQueue


class TestMyQueue(unittest.TestCase):

    def test_empty(self):
        q = MyQueue()
        self.assertRaises(ValueError, q.dequeue)

    def test_enqueue(self):
        q = MyQueue()
        q.enqueue(1)
        self.assertEquals(q.dequeue(), 1)

        q.enqueue(2)
        self.assertEquals(q.dequeue(), 2)

        q.enqueue(3)
        self.assertEquals(q.dequeue(), 3)

    def test_enqueue2(self):
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEquals(q.dequeue(), 1)
        self.assertEquals(q.dequeue(), 2)
        self.assertEquals(q.dequeue(), 3)
        self.assertEquals(q.dequeue(), 4)

    def test_mix(self):
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEquals(q.dequeue(), 1)
        q.enqueue(3)
        self.assertEquals(q.dequeue(), 2)
