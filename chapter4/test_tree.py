import unittest

import tree


class TestCompleteTree(unittest.TestCase):

    def test(self):
        t = tree.complete_tree(3)

        self.assertEquals(t.root.value, 0)
        self.assertEquals(t.root.left.value, 1)
        self.assertEquals(t.root.right.value, 2)
        self.assertEquals(t.root.left.left.value, 3)
        self.assertEquals(t.root.left.right.value, 4)
        self.assertEquals(t.root.right.left.value, 5)
        self.assertEquals(t.root.right.right.value, 6)

        self.assertEquals(t.root.left.left.left, None)
        self.assertEquals(t.root.left.left.right, None)
        self.assertEquals(t.root.left.right.left, None)
        self.assertEquals(t.root.left.right.right, None)
        self.assertEquals(t.root.right.left.left, None)
        self.assertEquals(t.root.right.left.right, None)
        self.assertEquals(t.root.right.right.left, None)
        self.assertEquals(t.root.right.right.right, None)
