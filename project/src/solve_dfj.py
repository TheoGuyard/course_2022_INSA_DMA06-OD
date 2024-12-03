import itertools
import numpy as np
import pulp


def solve_dfj(M):
    """
    Solves the TSP instance encoded in the adjacency matrix M by solving its
    Dantzig–Fulkerson–Johnson formulation.

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

    prob = pulp.LpProblem("TSP-DFJ", pulp.LpMinimize)
    varx = pulp.LpVariable.dicts(
        "x", [(i, j) for i in N for j in N if i != j], cat="Binary"
    )
    prob += pulp.lpSum([M[i, j] * varx[i, j] for i in N for j in N if i != j])
    for i in N:
        prob += pulp.lpSum([varx[i, j] for j in N if i != j]) == 1
        prob += pulp.lpSum([varx[j, i] for j in N if i != j]) == 1
    for s in range(2, len(N)):
        for Q in itertools.combinations(N, s):
            prob += (
                pulp.lpSum([varx[i, j] for i in Q for j in Q if i != j])
                <= s - 1
            )

    prob.solve(pulp.GUROBI_CMD(msg=0))

    return prob.objective.value()
