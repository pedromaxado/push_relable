import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from push_relable.classes import Graph
from push_relable.algorithms import push_relabel


def complete_graph_example(n, s, t):
    g = Graph(size=n)

    for u in range(n):
        for v in range(n):
            if u != v:
                g.add_edge(u, v, cap=1)

    print("finished building graph")

    start = timer()
    max_flow = push_relabel(g, s=s, t=t)
    duration = timer() - start

    print(f"Maximum flow: {max_flow}")
    print()

    return duration


def run_tests():

    durations = []

    for n in [i*10 for i in range(1, 40)]:
        duration = complete_graph_example(n, 0, 1)
        durations.append(duration)
        print(n, duration)

    print(durations)

    x = np.log(np.array([i*10 for i in range(1, 40)]))
    y = np.log(np.array(durations))

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    run_tests()
    # print(complete_graph_example(1000, 0, 1))
