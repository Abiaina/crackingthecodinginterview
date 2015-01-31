import unittest
from queue import Queue


class QueueTest(unittest.TestCase):

    def test_empty(self):
        queue = Queue([])
        self.assertRaises(ValueError, queue.peek)
        self.assertRaises(ValueError, queue.dequeue)

    def test_dequeue(self):
        queue = Queue("abcd")
        print repr(queue)
        self.assertEquals(queue.dequeue(), "a")
        self.assertEquals(queue.dequeue(), "b")
        self.assertEquals(queue.dequeue(), "c")
        self.assertEquals(queue.dequeue(), "d")

    def test_peek(self):
        queue = Queue("abcd")
        print repr(queue)
        self.assertEquals(queue.peek(), "a")
        self.assertEquals(queue.peek(), "a")

    def test_enqueue(self):
        queue = Queue("")
        queue.enqueue("a")
        self.assertEquals(queue.peek(), "a")
        queue.enqueue("b")
        self.assertEquals(queue.peek(), "a")
