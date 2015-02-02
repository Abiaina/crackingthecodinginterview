#
# Implement a function to check if a binary tree is balanced.  For the purposes
# of this question, a balanced tree is defined to be a tree such that the
# heights of the two subtrees of any node never differ by more than one.
#


def is_balanced(tree):
    return check_height(tree.root) != -1


def check_height(node):
    if node:
        left = check_height(node.left)
        if left == -1:
            return -1
        right = check_height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    else:
        return 0
