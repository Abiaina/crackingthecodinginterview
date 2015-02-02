class TreeNode(object):

    def __init__(self, value):
        self.value = value
        self.right = self.left = None


class Tree(object):

    def __init__(self):
        self.root = None


def complete_tree(height):
    assert height > 0
    tree = Tree()
    tree.root = TreeNode(0)
    counter = 1
    queue = [(height, tree.root)]
    while queue:
        node_height, node = queue.pop(0)
        if node_height == 1:
            continue
        node.left = TreeNode(counter)
        counter += 1
        queue.append((node_height - 1, node.left))

        node.right = TreeNode(counter)
        queue.append((node_height - 1, node.right))
        counter += 1
    return tree
