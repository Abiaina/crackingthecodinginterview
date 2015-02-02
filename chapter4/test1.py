import unittest
from tree import complete_tree, Tree

from problem1 import is_balanced


class TestIsBalanced(unittest.TestCase):

    def setUp(self):
        self.tree = complete_tree(3)

    def test_not_balanced(self):
        self.tree.root.right = None
        self.assertEquals(is_balanced(self.tree), False)

    def test_balanced(self):
        self.assertEquals(is_balanced(self.tree), True)

        self.tree.root.right.left = None
        self.tree.root.right.right = None
        self.assertEquals(is_balanced(self.tree), True)

    def test_empty(self):
        self.assertEquals(is_balanced(Tree()), True)

    def test_single(self):
        tree = complete_tree(1)
        self.assertEquals(is_balanced(tree), True)
