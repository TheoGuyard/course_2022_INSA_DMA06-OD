import argparse
import datetime
import numpy as np
import pathlib
import time
import tsplib95
from solve_ac import solve_ac
from solve_ct import solve_ct
from solve_dfj import solve_dfj
from solve_hk import solve_hk
from solve_lk import solve_lk
from solve_mtz import solve_mtz
from solve_nn import solve_nn


def load_instance(instance_name):
    path = pathlib.Path(__file__).parent.joinpath("instances", instance_name)
    prob = tsplib95.load(path)
    nodes = list(prob.get_nodes())
    edges = list(prob.get_edges())
    n = len(nodes)
    M = np.zeros((n, n))
    for edge in edges:
        i, j = edge
        M[i-1, j-1] = prob.get_weight(*edge)
        M[j-1, i-1] = prob.get_weight(*edge)
    return M


parser = argparse.ArgumentParser()
parser.add_argument("instance")
parser.add_argument(
    "method",
    choices=["ac", "ct", "dfj", "hk", "lk", "mtz", "nn"]
)

if __name__ == "__main__":
    args = parser.parse_args()

    print("Instance   : {}".format(args.instance))
    print("Method     : {}".format(args.method))

    M = load_instance(args.instance)

    t0 = time.time()
    if args.method == "ac":
        cost = solve_ac(M)
    if args.method == "ct":
        cost = solve_ct(M)
    elif args.method == "dfj":
        cost = solve_dfj(M)
    elif args.method == "hk":
        cost = solve_hk(M)
    elif args.method == "lk":
        cost = solve_lk(M)
    elif args.method == "mtz":
        cost = solve_mtz(M)
    elif args.method == "nn":
        cost = solve_nn(M)
    else:
        raise NotImplementedError
    t1 = time.time()

    print("Solve time : {}".format(datetime.timedelta(seconds=t1-t0)))
    print("Tour cost  : {}".format(cost))
