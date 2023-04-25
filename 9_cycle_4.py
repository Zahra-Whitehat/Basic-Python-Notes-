import networkx as nx

# example parity check matrix
H = [[1, 0, 1, 1],
     [1, 1, 0, 1],
     [0, 1, 1, 1]]

# construct the bipartite graph
B = nx.Graph()
for i, row in enumerate(H):
    for j, val in enumerate(row):
        if val == 1:
            B.add_edge(f'v{i}', f'c{j}')

# create the Tanner graph
T = nx.algorithms.bipartite.matrix.from_biadjacency_matrix(B.adjacency_matrix())

# check for cycles of length 4
for cycle in nx.cycle_basis(T):
    if len(cycle) == 4:
        print("Cycle of length 4 found:", cycle)
        break
else:
    print("No cycle of length 4 found.")
