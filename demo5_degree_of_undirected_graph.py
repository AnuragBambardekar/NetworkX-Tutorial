
import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(1,2),(2,3),(3,4),(4,5),(3,6),(6,7)]
G = nx.Graph() # a simple undirected graph
G.add_edges_from(edge_list)

print(nx.adjacency_matrix(G))

print(dict(G.degree)[2])

nx.draw_spring(G, with_labels=True)
plt.show()
