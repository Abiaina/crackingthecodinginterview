import unittest


def code(n):
    return ((n & (n - 1)) == 0)


class TestProblem4(unittest.TestCase):

    def test(self):
        self.assertEquals(code(1), 1)
        self.assertEquals(code(2), 1)
        self.assertEquals(code(3), 0)
        self.assertEquals(code(4), 1)
        self.assertEquals(code(5), 0)
        self.assertEquals(code(6), 0)
        self.assertEquals(code(7), 0)
        self.assertEquals(code(8), 1)
        self.assertEquals(code(9), 0)
        self.assertEquals(code(10), 0)
        self.assertEquals(code(11), 0)
        self.assertEquals(code(12), 0)
        self.assertEquals(code(13), 0)
        self.assertEquals(code(14), 0)
        self.assertEquals(code(15), 0)
        self.assertEquals(code(16), 1)

        self.assertEquals(code(32), 1)
        self.assertEquals(code(64), 1)
        self.assertEquals(code(128), 1)
        self.assertEquals(code(256), 1)
        self.assertEquals(code(512), 1)
        self.assertEquals(code(1024), 1)
