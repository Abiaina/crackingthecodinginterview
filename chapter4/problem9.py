#
# You are given a binary tree in which each node contains a value.
# Design an algorithm that prints all paths that sum to a given value.
# The path does not need to start or end at the root or leaf.
#
from __future__ import print_function


def path(tree, sums_to):
    path_node(tree.root, sums_to, sums_to, tree.root)


def path_node(node, sums_to, orig_sum, path_start, start_here=False):
    if node.value == sums_to:
        stack = []
        end = node
        while end != path_start:
            stack.append(end)
            end = end.parent
        stack.append(path_start)
        path = [n.value for n in reversed(stack)]
        # assert sum(path) == orig_sum
        print(path)
    if start_here:
        path_node(node, orig_sum, orig_sum, node)
    for child in [c for c in [node.left, node.right] if c]:
        path_node(child, sums_to - node.value, orig_sum, path_start, True)
