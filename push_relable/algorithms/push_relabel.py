"""
FIFO push-relabel algorithm for maximum flow problems.
"""

import numpy as np

from push_relable.classes import Graph


def _init_preflow(g, s, active_nodes):
    """

    Parameters
    ----------
    g : Graph
    s : int
    active_nodes : list

    Returns
    -------

    """

    for v in g.adj[s]:
        g.adj[s][v]['flow'] = g.adj[s][v]['cap']
        g.nodes[v]['excess'] = g.adj[s][v]['cap']
        g.nodes[s]['excess'] = g.nodes[s]['excess'] - g.adj[s][v]['cap']

        active_nodes.append(v)


def  _init_height(g, s, t):
    """

    Parameters
    ----------
    g
    s
    t

    Returns
    -------

    """

    queue = []
    visited = [False] * g.size

    visited[t] = True
    g.nodes[t]['height'] = 0
    queue.append(t)

    while queue:
        u = queue.pop(0)

        for v in g.adj[u]:
            if not visited[v]:
                queue.append(v)
                g.nodes[v]['height'] = g.nodes[u]['height'] + 1
                visited[v] = True

    g.nodes[s]['height'] = g.size


def _push(g, edge):
    pass


def _relabel(g, v):
    pass


def _discharge(g, v, active_nodes):
    pass


def push_relabel(g, s, t):
    """

    Parameters
    ----------
    g : Graph
    s : node
    t : node

    Returns
    -------
    max_flow : int

    """

    res_g = build_residual_graph(g)

    active_nodes = []

    _init_preflow(res_g, s, active_nodes)
    _init_height(res_g, s, t)

    for idx, v in enumerate(res_g.nodes):
        print(idx, v)

    print()

    for e in res_g.edges:
        print(e)

    #while active_nodes:

    #    v = active_nodes.pop(0)

    #    if res_g.nodes[v]['excess'] > 0:
    #        _discharge(res_g, v, active_nodes)

    return res_g.nodes[t]['excess']


def build_residual_graph(g):
    """

    Parameters
    ----------
    g : Graph

    Returns
    -------

    """

    res_g = Graph(g.size)

    for u in range(g.size):
        res_g.set_node_prop(u, excess=0, height=np.inf)

    for u, v, datadict in g.edges:
        if not res_g.has_edge(u, v):
            res_g.add_edge(u, v, cap=datadict['cap'], flow=0)
            res_g.add_edge(v, u, cap=0, flow=0)
        else:
            res_g.add_edge(u, v, cap=datadict['cap'], flow=0)

    return res_g


if __name__ == '__main__':

    g = Graph(size=5)

    g.add_edge(0, 1, cap=12)
    g.add_edge(0, 2, cap=14)
    g.add_edge(1, 2, cap=5)
    g.add_edge(1, 3, cap=8)
    g.add_edge(2, 3, cap=8)
    g.add_edge(3, 4, cap=10)
    g.add_edge(1, 4, cap=16)
    g.add_edge(3, 1, cap=7)

    push_relabel(g, s=0, t=4)
