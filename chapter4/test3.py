import unittest
from problem3 import create_bst
from problem5 import is_bst
from tree import complete_tree


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


class TestHeight(unittest.TestCase):

    def test(self):
        tree = complete_tree(3)
        self.assertEquals(height(tree.root), 3)


class TestCreateBst(unittest.TestCase):

    def test(self):
        arr = range(63)
        tree = create_bst(arr)
        self.assertEquals(height(tree.root), 6)
        self.assertEquals(is_bst(tree), True)
