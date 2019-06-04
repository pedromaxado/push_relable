"""Base class for directed graphs.

"""


class Graph:
    """
    Base class for directed graphs.

    """

    _size = None

    def __init__(self, size):
        """

        Parameters
        ----------
        size : int
            The number of vertex the graph have.

        """

        self.size = size

        self.nodes = [{} for i in range(size)]
        self.adj = [{} for i in range(size)]

    def set_node_prop(self, u, **attr):

        self.nodes[u].update(attr)

    def add_edge(self, u, v, **attr):

        if v not in self.adj[u]:
            self.adj[u][v] = {}

        self.adj[u][v].update(attr)

    def has_edge(self, u, v):

        try:
            return v in self.adj[u]
        except KeyError:
            return False

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def edges(self):

        edges = []

        for u in range(self.size):
            for v in self.adj[u]:
                edges.append((u, v, self.adj[u][v]))

        return edges
