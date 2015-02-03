#
# Write an algorithm to find the "next" node (i.e. in-order traversal) of a
# given node in a binary search tree.  You may assume that each node has a link
# to its parent.
#


def next_node(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent:
        if node == node.parent.left:
            return node.parent
        node = node.parent
    return None
