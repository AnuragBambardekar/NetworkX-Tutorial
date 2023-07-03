
import networkx as nx
import matplotlib.pyplot as plt

# Constructing graph from list of edges

edge_list = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
G = nx.Graph() # a simple undirected graph
G.add_edges_from(edge_list)

print(nx.adjacency_matrix(G))

nx.draw_spring(G, with_labels=True)
plt.show()

nx.draw_planar(G, with_labels=True)
plt.show()