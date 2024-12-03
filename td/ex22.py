import numpy as np
import networkx as nx

data = [
    ("s", "a", 3),
    ("s", "c", 5),
    ("a", "b", np.inf),
    ("c", "a", 5),
    ("c", "t", 2),
    ("b", "c", 2),
    ("b", "t", 6)
]

G = nx.DiGraph()
for s, t, c in data:
    G.add_edge(s, t, capacity=c)

fv, fd = nx.maximum_flow(G, "s", "t")
print(fv)
print(fd)