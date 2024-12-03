import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

n = 4
H = [15     , 20    , 23    , 30    ]
L = [100    , 300   , 200   , 300   ]
F = [1000   , 1200  , 1100  , 1600  ]
C = [5      , 6     , 7     , 9     ]

def cost(i, j):
    if j <= i:
        return np.inf
    return F[j-1] + C[j-1] * sum(L[k] for k in range(i,j))

G = nx.DiGraph()
for j in range(n+1):
    for i in range(j):
        c = cost(i, j)
        if c < np.inf:
            G.add_edge(i, j, weight=c)

for (u, v, wt) in G.edges.data('weight'):
    print(f"({u}, {v}, {wt})")

print(nx.shortest_path(G, source=0, target=4, weight='weight'))