"""
FIFO push-relabel algorithm for maximum flow problems.
"""

import numpy as np

from push_relable.classes import Graph


def _init_preflow(res_g, s, active_nodes):
    """

    Parameters
    ----------
    res_g : Graph
    s : int
    active_nodes : (list)

    Returns
    -------

    """

    for v in res_g.adj[s]:
        res_g.adj[s][v]['flow'] = res_g.adj[s][v]['cap']
        res_g.nodes[v]['excess'] = res_g.adj[s][v]['cap']
        res_g.nodes[s]['excess'] = res_g.nodes[s]['excess'] - res_g.adj[s][v]['cap']

        active_nodes.append(v)


def _init_height(res_g, s, t):
    """

    Parameters
    ----------
    res_g
    s
    t

    Returns
    -------

    """

    queue = []
    visited = [False] * res_g.size

    visited[t] = True
    res_g.nodes[t]['height'] = 0
    queue.append(t)

    while queue:
        u = queue.pop(0)

        for v in res_g.adj[u]:
            if not visited[v]:
                queue.append(v)
                res_g.nodes[v]['height'] = res_g.nodes[u]['height'] + 1
                visited[v] = True

    res_g.nodes[s]['height'] = res_g.size


def _push(res_g, u, v, s, t, active_nodes):

    edge = res_g.adj[u][v]

    amount = min(res_g.nodes[u]['excess'], edge['cap'] - edge['flow'])

    edge[u][v]['flow'] += amount
    edge[v][u]['flow'] -= amount

    if res_g.nodes[v]['excess'] == 0 and v not in [s, t]:
        active_nodes.append(v)

    res_g.nodes[u]['excess'] -= amount
    res_g.nodes[v]['excess'] += amount


def _relabel(res_g, v):

    min_h = np.inf

    # TODO: implementar relabel

    res_g.nodes[v]['height'] = min_h


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

    # while active_nodes:

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
