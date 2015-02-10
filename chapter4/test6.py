import unittest

import problem3
import problem6


class Visitor(object):

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            self.visit(node)
            self.in_order(node.right)

    def visit(self, node):
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node


def add_parent_pointers(tree):
    visitor = Visitor()
    visitor.in_order(tree.root)
    tree.root.parent = None


class TestNextNode(unittest.TestCase):

    def setUp(self):
        self.tree = problem3.create_bst(range(7))
        add_parent_pointers(self.tree)

    def test_complete(self):
        node = self.tree.root.left.left
        self.assertEquals(node.left, None)
        self.assertEquals(node.right, None)
        self.assertEquals(node.value, 0)

        node = problem6.next_node(node)
        self.assertEquals(node.value, 1)

        node = problem6.next_node(node)
        self.assertEquals(node.value, 2)

        node = problem6.next_node(node)
        self.assertEquals(node.value, 3)

        node = problem6.next_node(node)
        self.assertEquals(node.value, 4)

        node = problem6.next_node(node)
        self.assertEquals(node.value, 5)

        node = problem6.next_node(node)
        self.assertEquals(node.value, 6)
