import unittest
import test6
import problem3
import problem7


class TestLowestCommonAncestor(unittest.TestCase):

    def setUp(self):
        self.t = problem3.create_bst(range(7))
        test6.add_parent_pointers(self.t)

    def test_none(self):
        self.assertEquals(problem7.lca(self.t.root, None), None)
        self.assertEquals(problem7.lca(None, self.t.root), None)
        self.assertEquals(problem7.lca(None, None), None)

    def test_same_node(self):
        self.assertEquals(problem7.lca(self.t.root, self.t.root), self.t.root)
        self.assertEquals(problem7.lca(self.t.root.left, self.t.root.left),
                          self.t.root.left)

    def test_simple(self):
        self.assertEquals(problem7.lca(self.t.root.left, self.t.root.right),
                          self.t.root)

    def test_hard(self):
        self.assertEquals(problem7.lca(self.t.root.left.right,
                                       self.t.root.right),
                          self.t.root)
