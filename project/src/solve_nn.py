import numpy as np


def solve_nn(M):
    """
    Solves the TSP instance encoded in the adjacency matrix M by using a
    Nearest-Neighbor heuristic.

    Arguments
    ---------
    M : np.ndarray
        The adjacency matrix.

    Returns
    -------
    cost : int or float
        The solution tour cost.
    """

    n = M.shape[0]
    locs = set(range(1, n))
    tour = [0]
    cost = 0
    while locs:
        curr = tour[-1]
        near = min(locs, key=lambda x: M[curr, x])
        tour.append(near)
        locs.remove(near)
        cost += M[curr, near]
    tour.append(0)

    return cost
