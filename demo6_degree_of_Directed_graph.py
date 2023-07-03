
import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(1,2),(2,3),(3,4),(4,5),(3,6),(6,7)]
G = nx.DiGraph() # a simple directed graph
G.add_edges_from(edge_list)

print(nx.adjacency_matrix(G))

print(dict(G.in_degree)[3])
print(dict(G.out_degree)[3])
print(dict(G.degree)[3])

nx.draw_spring(G, with_labels=True)
plt.show()
