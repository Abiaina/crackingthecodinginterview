import unittest

from tree import complete_tree


class TestCompleteTree(unittest.TestCase):

    def test(self):
        tree = complete_tree(3)

        self.assertEquals(tree.root.value, 0)
        self.assertEquals(tree.root.left.value, 1)
        self.assertEquals(tree.root.right.value, 2)
        self.assertEquals(tree.root.left.left.value, 3)
        self.assertEquals(tree.root.left.right.value, 4)
        self.assertEquals(tree.root.right.left.value, 5)
        self.assertEquals(tree.root.right.right.value, 6)

        self.assertEquals(tree.root.left.left.left, None)
        self.assertEquals(tree.root.left.left.right, None)
        self.assertEquals(tree.root.left.right.left, None)
        self.assertEquals(tree.root.left.right.right, None)
        self.assertEquals(tree.root.right.left.left, None)
        self.assertEquals(tree.root.right.left.right, None)
        self.assertEquals(tree.root.right.right.left, None)
        self.assertEquals(tree.root.right.right.right, None)
