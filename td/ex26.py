import string
import numpy as np
import networkx as nx
from networkx.algorithms import bipartite

# C = np.array([
#     [np.inf, 8, 7],
#     [     7, 6, 4],
#     [     3, 3, 3],
# ])

C = np.array([
    [17, 15,  9,  5, 12],
    [16, 16, 10,  5, 10],
    [12, 15, 14, 11,  5],
    [ 4,  8, 14, 17, 13],
    [13,  9,  8, 12, 17],
])


G = nx.Graph()
for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        G.add_edge(i, string.ascii_letters[j], weight=C[i,j])

assert bipartite.is_bipartite(G)


M = bipartite.minimum_weight_full_matching(G)
print(M)
