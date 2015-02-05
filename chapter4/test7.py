import unittest
from test6 import add_parent_pointers
from problem3 import create_bst
from problem7 import lowest_common_ancestor as lca


class TestLowestCommonAncestor(unittest.TestCase):

    def setUp(self):
        self.tree = create_bst(range(7))
        add_parent_pointers(self.tree)

    def test_none(self):
        self.assertEquals(lca(self.tree.root, None), None)
        self.assertEquals(lca(None, self.tree.root), None)
        self.assertEquals(lca(None, None), None)

    def test_same_node(self):
        self.assertEquals(lca(self.tree.root, self.tree.root), self.tree.root)
        self.assertEquals(lca(self.tree.root.left, self.tree.root.left),
                          self.tree.root.left)

    def test_simple(self):
        self.assertEquals(lca(self.tree.root.left, self.tree.root.right),
                          self.tree.root)

    def test_hard(self):
        self.assertEquals(lca(self.tree.root.left.right, self.tree.root.right),
                          self.tree.root)
