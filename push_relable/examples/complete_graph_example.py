import numpy as np

from push_relable.classes import Graph
from push_relable.algorithms import push_relabel


def complete_graph_example(n):
    g = Graph(size=n)

    for u in range(n):
        for v in range(n):
            if u != v:
                g.add_edge(u, v, cap=np.random.randint(1, 10))

    max_flow = push_relabel(g, s=0, t=9)

    print(f"Maximum flow: {max_flow}")


if __name__ == '__main__':
    complete_graph_example(50)
