class DirectedGraph(object):

    def __init__(self, nodes):
        assert len(nodes) == len(set(nodes))
        self.nodes = nodes
        self.adj = []
        for _ in enumerate(nodes):
            self.adj.append([0] * len(nodes))

    def add_edge(self, source, dest):
        if source not in self.nodes:
            raise ValueError("invalid source node")
        if dest not in self.nodes:
            raise ValueError("invalid destination node")
        source_idx = self.nodes.index(source)
        dest_idx = self.nodes.index(dest)
        self.adj[source_idx][dest_idx] = 1

    def neighbors(self, source):
        if source not in self.nodes:
            raise ValueError("invalid source node")
        source_idx = self.nodes.index(source)
        neigh_idx = [i for (i, j) in enumerate(self.adj[source_idx]) if j]
        return [self.nodes[i] for i in neigh_idx]
