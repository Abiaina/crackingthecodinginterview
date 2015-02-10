import unittest

import problem3
import problem5
import tree


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


class TestHeight(unittest.TestCase):

    def test(self):
        t = tree.complete_tree(3)
        self.assertEquals(height(t.root), 3)


class TestCreateBst(unittest.TestCase):

    def test(self):
        arr = range(63)
        t = problem3.create_bst(arr)
        self.assertEquals(height(t.root), 6)
        self.assertEquals(problem5.is_bst(t), True)
