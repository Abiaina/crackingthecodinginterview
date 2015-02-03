import unittest
from problem3 import create_bst
from tree import complete_tree, Tree, TreeNode


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_bst(node):
    if node is None:
        return True
    if node.left and node.right and node.left.value > node.right.value:
        return False
    return is_bst(node.left) and is_bst(node.right)


class TestHeight(unittest.TestCase):

    def test(self):
        tree = complete_tree(3)
        self.assertEquals(height(tree.root), 3)


class TestIsBst(unittest.TestCase):

    def test_positive(self):
        tree = Tree()
        tree.root = TreeNode(2)
        tree.root.left = TreeNode(1)
        tree.root.right = TreeNode(3)
        self.assertEquals(is_bst(tree.root), True)

    def test_negative(self):
        tree = Tree()
        tree.root = TreeNode(2)
        tree.root.left = TreeNode(3)
        tree.root.right = TreeNode(1)
        self.assertEquals(is_bst(tree.root), False)


class TestCreateBst(unittest.TestCase):

    def test(self):
        arr = range(63)
        tree = create_bst(arr)
        self.assertEquals(height(tree.root), 6)
        self.assertEquals(is_bst(tree.root), True)
