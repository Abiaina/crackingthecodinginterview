def is_subtree(huge, tiny):
    if huge.root is None:
        return False
    stack = [huge.root]
    while stack:
        node = stack.pop()
        if helper(node, tiny.root):
            return True
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


def helper(huge, tiny):
    if tiny is None:
        return True
    elif huge is None or huge.value != tiny.value:
        return False
    return helper(huge.left, tiny.left) and helper(huge.right, tiny.right)
