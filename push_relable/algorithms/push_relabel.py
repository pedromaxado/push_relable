"""
FIFO push-relabel algorithm for maximum flow problems.
"""

from push_relable.classes import Graph


def push_relabel(g, s, t):

    res_g = build_residual_graph(g)


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
        res_g.set_node_prop(u, excess=0, height=0)



    return res_g
