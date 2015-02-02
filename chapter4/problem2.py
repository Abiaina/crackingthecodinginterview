#
# Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.
#


def path_exists(graph, source, dest):
    queue = [source]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node == dest:
            return True
        elif node in visited:
            continue
        queue.extend(graph.neighbors(node))
    return False
