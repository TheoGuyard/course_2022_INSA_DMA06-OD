import numpy as np


def solve_hk(M):
    """
    Solves the TSP instance encoded in the adjacency matrix M by using the
    Held-Karp algorithm.

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
    N = range(n)
    D = np.full((1 << n, n), np.inf)
    D[1, 0] = 0

    for m in range(1 << n):
        for k in N:
            if not (m & (1 << k)):
                continue
            p = m ^ (1 << k)
            if p == 0:
                continue
            for c in N:
                if c == k or not (p & (1 << c)):
                    continue
                D[m, k] = min(D[m, k], D[p, c] + M[c, k])

    return min(D[(1 << n) - 1, i] + M[i, 0] for i in range(1, n))
