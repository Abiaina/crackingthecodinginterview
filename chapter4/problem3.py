#
# Given a sorted (increasing order) array with unique integer elements, write
# an algorithm to create a binary search tree with minimum height.
#

from tree import Tree, TreeNode


def create_subtree(arr):
    if len(arr) == 0:
        return None
    idx = len(arr) / 2
    node = TreeNode(arr[idx])
    node.left = create_subtree(arr[:idx])
    node.right = create_subtree(arr[idx+1:])
    return node


def create_bst(arr):
    tree = Tree()
    tree.root = create_subtree(arr)
    return tree
