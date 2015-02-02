#
# Implement a function to check if a binary tree is balanced.  For the purposes
# of this question, a balanced tree is defined to be a tree such that the
# heights of the two subtrees of any node never differ by more than one.
#


def is_balanced(tree):
    heights = {}
    return is_balanced_node(tree.root, heights)


def is_balanced_node(node, heights):
    if node:
        bal = is_balanced_node(node.left, heights)
        if not bal:
            return False
        bal = is_balanced_node(node.right, heights)
        if not bal:
            return False
        heights[node] = 1 + max(heights[node.left], heights[node.right])
        return abs(heights[node.left] - heights[node.right]) <= 1
    else:
        heights[node] = 0
        return True
