#
# Given a binary tree, design an algorithm which creates a linked list of all
# th enodes at each depth (e.g. if you have a tree with depth D, you'll have
# D linked lists).
#


def slice_tree(tree):
    queue = [(0, tree.root)]
    slices = []
    prev_depth = -1
    while queue:
        depth, node = queue.pop(0)
        if depth != prev_depth:
            slices.append([])
            prev_depth = depth
        slices[-1].append(node)
        for child in [node.left, node.right]:
            if child:
                queue.append((depth + 1, child))
    return slices
