import numpy as np


def nn_algo(init_node, cost_matrix, n_nodes):
    """
    Nearest Neighbour algorithm
    """
    cost_matrix = cost_matrix.copy()

    for i in range(n_nodes):
        cost_matrix[i][i] = np.inf

    tour = [init_node]

    for _ in range(n_nodes - 1):
        node = tour[-1]
        min_index = np.argmin(cost_matrix[node])
        for t in tour:
            cost_matrix[min_index][t] = np.inf
            cost_matrix[t][min_index] = np.inf
        tour.append(min_index)
    tour.append(init_node)
    return tour
