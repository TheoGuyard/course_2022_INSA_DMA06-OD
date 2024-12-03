import itertools
import networkx as nx
import pulp


def solve_ct(M):
    """
    Solves the TSP instance encoded in the adjacency matrix M by using an
    algorithm that is intended to be the fastest among all the groups.

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

    # Warm-start with trivial sub-tours with 2 vertices
    for Q in itertools.combinations(N, 2):
        prob += pulp.lpSum(varx[i, j] for i in Q for j in Q if i != j) <= 1

    # print("{:>4} | {:>5} | {:>7}".format("iter", "cuts", "obj"))

    iter = 0
    cuts = 0
    while True:

        iter += 1

        # Solve
        prob.solve(pulp.GUROBI_CMD(msg=0))

        # Find sub-tours in the solution
        E = [
            (i, j) for i in N for j in N if i != j and varx[i, j].varValue > 0
        ]
        G = nx.DiGraph(E)
        C = list(nx.simple_cycles(G))

        # Add cuts corresponding to sub-tours found
        for Q in C:
            prob += pulp.lpSum(
                varx[i, j] for i in Q for j in Q if i != j
            ) <= len(Q) - 1
            cuts += 1

        # Displays
        # print("{:4} | {:5} | {:7}".format(iter, cuts, prob.objective.value()))

        # Stop if only one cycle is found
        if len(C) == 1:
            break

    # print(f"Opt. tour  : {C[0]}")

    return prob.objective.value()
