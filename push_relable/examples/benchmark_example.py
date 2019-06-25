import os
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from timeit import default_timer as timer
from push_relable.classes import Graph
from push_relable.algorithms import push_relabel


GRAPH_GEN_PATH = "/home/pedro/Dropbox/MatComp/3-periodo/AEDS-III/TPs/tp1/tests/graph.py"
GRAPH_OUT_PATH = "/tmp/graph.txt"


def generate_graph_file(n, m):
    os.system(GRAPH_GEN_PATH + " -u -k -e " + str(m) + " " + str(n) + " > " + GRAPH_OUT_PATH)


def read_graph_from_file(n):

    g = Graph(size=n)

    with open(GRAPH_OUT_PATH, "r") as fp:
        for line in fp:
            e = list(map(int, line.strip().split(' ')))
            g.add_edge(u=e[0], v=e[1], cap=1)

    # pprint(g.edges)

    return g


def time_push_relabel(n, m):

    generate_graph_file(n, m)
    g = read_graph_from_file(n)

    s = np.random.randint(0, n)
    t = np.random.randint(0, n)

    # while s == t:
    #     t = np.random.randint(0, n)

    start = timer()
    max_flow = push_relabel(g=g, s=0, t=n-1)
    end = timer() - start

    return end


def plot_all_the_crap(x, y):

    for y_values in y:
        plt.plot(x, y_values, '--')

    plt.show()


def plot_all_the_crap_log(x, y):

    x_log = np.log(np.array(x))

    for y_values in y:
        plt.plot(x_log, np.log(y_values), '--')

    plt.show()


def run_benchmark():

    max_n = 6
    max_rep = 10

    v_sizes = [i*10 for i in range(1, max_n)]
    densities = [0.1*i for i in range(1, 11)]

    y_values = []

    for d in densities:
        print("density="+str(d))

        y_values.append([])

        for n in v_sizes:
            print("n="+str(n), end="")
            m = max(int((n*(n-1)/2)*d), n-1)

            avg = 0

            for i in range(max_rep):
                avg += time_push_relabel(n, m)

            avg /= max_rep
            print(", time="+str(avg))

            y_values[-1].append(avg)

    plot_all_the_crap(v_sizes, y_values)
    plot_all_the_crap_log(v_sizes, y_values)


if __name__ == '__main__':
    run_benchmark()
