import unittest
import digraph


class TestDigraph(unittest.TestCase):

    def setUp(self):
        self.g = digraph.DirectedGraph(range(6))

        self.g.add_edge(0, 1)
        self.g.add_edge(0, 2)
        self.g.add_edge(0, 4)
        self.g.add_edge(2, 3)
        self.g.add_edge(3, 4)
        self.g.add_edge(4, 0)

    def test_constructor(self):
        self.assertEquals(len(self.g.adj), 6)
        self.assertEquals(len(self.g.adj[0]), 6)
        self.assertEquals(len(self.g.adj[1]), 6)
        self.assertEquals(len(self.g.adj[2]), 6)
        self.assertEquals(len(self.g.adj[3]), 6)
        self.assertEquals(len(self.g.adj[4]), 6)
        self.assertEquals(len(self.g.adj[5]), 6)

    def test_neighbors(self):
        self.assertEquals(self.g.neighbors(0), [1, 2, 4])
        self.assertEquals(self.g.neighbors(1), [])
        self.assertEquals(self.g.neighbors(2), [3])
        self.assertEquals(self.g.neighbors(3), [4])
        self.assertEquals(self.g.neighbors(4), [0])
        self.assertEquals(self.g.neighbors(5), [])

        self.assertRaises(ValueError, self.g.neighbors, 8)

    def test_add_edge(self):
        self.assertRaises(ValueError, self.g.add_edge, 6, 7)
        self.assertRaises(ValueError, self.g.add_edge, 6, 1)
        self.assertRaises(ValueError, self.g.add_edge, 1, 7)
