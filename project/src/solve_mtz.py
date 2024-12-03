import numpy as np
import pulp


def solve_mtz(M):
    """
    Solves the TSP instance encoded in the adjacency matrix M by solving its
    Miller–Tucker–Zemlin formulation.

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

    prob = pulp.LpProblem("TSP-MTZ", pulp.LpMinimize)
    varx = pulp.LpVariable.dicts(
        "x", [(i, j) for i in N for j in N if i != j], cat="Binary"
    )
    varu = pulp.LpVariable.dicts(
        "u", [i for i in N if i != 0], cat="Integer", lowBound=1, upBound=n
    )

    prob += pulp.lpSum([M[i, j] * varx[i, j] for i in N for j in N if i != j])
    for i in N:
        prob += pulp.lpSum([varx[i, j] for j in N if i != j]) == 1
        prob += pulp.lpSum([varx[j, i] for j in N if i != j]) == 1
        for j in N:
            if i != j and (i != 0 and j != 0):
                prob += varu[i] - varu[j] + (n - 1) * varx[i, j] <= n - 2

    prob.solve(pulp.GUROBI_CMD(msg=0))

    return prob.objective.value()
