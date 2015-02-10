#
# Design an algorithm and write code to find the most common ancestor of two
# nodes in a binary tree.  Avoid storing additional nodes in a data structure.
# NOTE: this is not necessarily a binary search tree.
#


def find_depth(node):
    counter = 0
    while node.parent:
        counter += 1
        node = node.parent
    return counter


def lca(shallow, deep):
    if shallow is None or deep is None:
        return None
    shallow_depth = find_depth(shallow)
    deep_depth = find_depth(deep)
    if shallow_depth > deep_depth:
        shallow_depth, deep_depth = deep_depth, shallow_depth
        shallow, deep = deep, shallow
    for _ in xrange(deep_depth - shallow_depth):
        deep = deep.parent
    while deep != shallow:
        if (deep.parent is None) or (shallow.parent is None):
            return None
        deep = deep.parent
        shallow = shallow.parent
    return deep
