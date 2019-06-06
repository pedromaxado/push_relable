from push_relable.classes import Graph
from push_relable.algorithms import push_relabel


def cormen_example():
    g = Graph(size=5)

    g.add_edge(0, 1, cap=12)
    g.add_edge(0, 2, cap=14)
    g.add_edge(1, 2, cap=5)
    g.add_edge(2, 3, cap=8)
    g.add_edge(3, 4, cap=10)
    g.add_edge(1, 4, cap=16)
    g.add_edge(3, 1, cap=7)

    max_flow = push_relabel(g, s=0, t=4)

    print(f"Maximum flow: {max_flow}")


if __name__ == '__main__':
    cormen_example()
