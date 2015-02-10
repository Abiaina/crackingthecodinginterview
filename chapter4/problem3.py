#
# Given a sorted (increasing order) array with unique integer elements, write
# an algorithm to create a binary search tree with minimum height.
#

import tree


def create_subtree(arr):
    if len(arr) == 0:
        return None
    idx = len(arr) / 2
    node = tree.Node(arr[idx])
    node.left = create_subtree(arr[:idx])
    node.right = create_subtree(arr[idx+1:])
    return node


def create_bst(arr):
    t = tree.Tree()
    t.root = create_subtree(arr)
    return t
