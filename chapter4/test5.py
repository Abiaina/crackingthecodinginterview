import unittest

import problem5
import tree


class TestIsBst(unittest.TestCase):

    def test_positive(self):
        t = tree.Tree()
        t.root = tree.Node(2)
        t.root.left = tree.Node(1)
        t.root.right = tree.Node(3)
        self.assertEquals(problem5.is_bst(t), True)

    def test_negative(self):
        t = tree.Tree()
        t.root = tree.Node(2)
        t.root.left = tree.Node(3)
        t.root.right = tree.Node(1)
        self.assertEquals(problem5.is_bst(t), False)
