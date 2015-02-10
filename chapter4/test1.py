import unittest

import tree
import problem1


class TestIsBalanced(unittest.TestCase):

    def setUp(self):
        self.tree = tree.complete_tree(3)

    def test_not_balanced(self):
        self.tree.root.right = None
        self.assertEquals(problem1.is_balanced(self.tree), False)

    def test_balanced(self):
        self.assertEquals(problem1.is_balanced(self.tree), True)

        self.tree.root.right.left = None
        self.tree.root.right.right = None
        self.assertEquals(problem1.is_balanced(self.tree), True)

    def test_empty(self):
        self.assertEquals(problem1.is_balanced(tree.Tree()), True)

    def test_single(self):
        t = tree.complete_tree(1)
        self.assertEquals(problem1.is_balanced(t), True)
