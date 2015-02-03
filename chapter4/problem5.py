#
# Implement a function to check if a binary tree is a binary search tree.
#


def is_bst_subtree(node):
    if node is None:
        return True
    if node.left and node.right and node.left.value > node.right.value:
        return False
    return is_bst_subtree(node.left) and is_bst_subtree(node.right)


def is_bst(tree):
    return is_bst_subtree(tree.root)
