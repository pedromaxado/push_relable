import os
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from timeit import default_timer as timer
from push_relable.utils import generate_digraph
from push_relable.classes import Graph
from push_relable.algorithms import push_relabel


def read_graph_from_generator(n, edges):

    g = Graph(size=n)

    for e in edges:
        g.add_edge(u=e[0], v=e[1], cap=e[2])

    return g


def time_push_relabel(n, m):

    edges = generate_digraph(n, m)
    g = read_graph_from_generator(n, edges)

    st = np.random.choice(n, 2, replace=False)

    start = timer()
    max_flow = push_relabel(g=g, s=st[0], t=st[1])
    end = timer() - start

    return end


def plot_all_the_crap(x, y):

    d = 0.1

    for y_values in y:
        plt.plot(x, y_values, '--', label="d = {:.2f}".format(d))
        d += 0.1

    plt.xlabel('Número de vértices')
    plt.ylabel('Tempo de execução (s)')
    plt.legend()

    plt.savefig('/home/pedro/exec_time.eps', format='eps', dpi=1000)
    plt.show()


def plot_all_the_crap_log(x, y):

    d = 0.1
    x_log = np.log(np.array(x))

    for y_values in y:
        plt.plot(x_log, np.log(y_values), '--', label="d = {:.2f}".format(d))
        d += 0.1

    plt.xlabel('Número de vértices')
    plt.ylabel('Tempo de execução (s)')
    plt.legend()

    plt.savefig('/home/pedro/exec_time_log.eps', format='eps', dpi=1000)
    plt.show()


def run_benchmark():

    min_n = 1
    max_n = 16
    max_rep = 15

    v_sizes = [i*10 for i in range(min_n, max_n)]
    densities = [0.1*i for i in range(1, 11)]

    y_values = []

    for d in densities:
        print("density="+str(d))

        y_values.append([])

        for n in v_sizes:
            print("n="+str(n), end="")
            m = max(int((n*(n-1))*d), n-1)

            avg = 0.0

            for i in range(max_rep):
                avg += time_push_relabel(n, m)

            avg /= max_rep
            print(", time="+str(avg))

            y_values[-1].append(avg)

    with open('/home/pedro/test_data.txt', 'w') as fp:
        fp.writelines(str(v_sizes))
        fp.writelines("\n")
        fp.writelines(str(y_values))

    plot_all_the_crap(v_sizes, y_values)
    plot_all_the_crap_log(v_sizes, y_values)


if __name__ == '__main__':
    run_benchmark()
