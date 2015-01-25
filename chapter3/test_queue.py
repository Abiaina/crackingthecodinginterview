import unittest
from queue import Queue


class QueueTest(unittest.TestCase):

    def test_empty(self):
        queue = Queue([])
        self.assertRaises(ValueError, queue.peek)
        self.assertRaises(ValueError, queue.pop)

    def test_pop(self):
        queue = Queue("abcd")
        print repr(queue)
        self.assertEquals(queue.pop(), "a")
        self.assertEquals(queue.pop(), "b")
        self.assertEquals(queue.pop(), "c")
        self.assertEquals(queue.pop(), "d")

    def test_peek(self):
        queue = Queue("abcd")
        print repr(queue)
        self.assertEquals(queue.peek(), "a")
        self.assertEquals(queue.peek(), "a")

    def test_push(self):
        queue = Queue("")
        queue.push("a")
        self.assertEquals(queue.peek(), "a")
        queue.push("b")
        self.assertEquals(queue.peek(), "a")
