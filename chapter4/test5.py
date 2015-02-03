import unittest
from problem5 import is_bst
from tree import Tree, TreeNode


class TestIsBst(unittest.TestCase):

    def test_positive(self):
        tree = Tree()
        tree.root = TreeNode(2)
        tree.root.left = TreeNode(1)
        tree.root.right = TreeNode(3)
        self.assertEquals(is_bst(tree), True)

    def test_negative(self):
        tree = Tree()
        tree.root = TreeNode(2)
        tree.root.left = TreeNode(3)
        tree.root.right = TreeNode(1)
        self.assertEquals(is_bst(tree), False)
