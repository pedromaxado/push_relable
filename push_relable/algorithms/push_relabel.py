"""
FIFO push-relabel algorithm for maximum flow problems.
"""

import numpy as np

from push_relable.classes import Graph


def _is_edge_valid(res_g, u, v):
    """

    Parameters
    ----------
    res_g : Graph
    u : int
    v : int

    Returns
    -------

    """

    residual_cap = res_g.adj[u][v]['cap'] - res_g.adj[u][v]['flow']

    return residual_cap > 0 and res_g.nodes[u]['height'] == res_g.nodes[v]['height'] + 1


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
        res_g.adj[v][s]['flow'] = -res_g.adj[s][v]['cap']
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

    res_g.adj[u][v]['flow'] += amount
    res_g.adj[v][u]['flow'] -= amount

    if res_g.nodes[v]['excess'] == 0 and v not in [s, t]:
        active_nodes.append(v)

    res_g.nodes[u]['excess'] -= amount
    res_g.nodes[v]['excess'] += amount


def _relabel(res_g, u):

    min_h = np.inf

    for v in res_g.adj[u]:  # verificar se n tem q olhar os arcos de volta (v, u)
        if res_g.adj[u][v]['cap'] - res_g.adj[u][v]['flow'] > 0:
            min_h = min(min_h, res_g.nodes[v]['height'])

    res_g.nodes[u]['height'] = min_h + 1


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

    while active_nodes:

        u = active_nodes.pop(0)

        for v in res_g.adj[u]:
            if _is_edge_valid(res_g, u, v):
                _push(res_g, u, v, s, t, active_nodes)

        if res_g.nodes[u]['excess'] > 0:
            _relabel(res_g, u)
            active_nodes.append(u)

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
