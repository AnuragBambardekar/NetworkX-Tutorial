# pip install networkx

import networkx as nx
import matplotlib.pyplot as plt

# Constructing graph from list of edges

edge_list = [(1,2),(2,3),(3,4),(4,5),(3,6),(6,7)]
G = nx.Graph() # a simple undirected graph
G.add_edges_from(edge_list)

print(nx.adjacency_matrix(G))

nx.draw_spring(G, with_labels=True)
plt.show()

nx.draw_circular(G, with_labels=True)
plt.show()

nx.draw_shell(G, with_labels=True)
plt.show()

nx.draw_spectral(G, with_labels=True)
plt.show()

nx.draw_random(G, with_labels=True)
plt.show()

nx.draw_planar(G, with_labels=True)
plt.show()

#=============================================================================#

# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt

# # Constructing graph from nummpy array
# G = nx.from_numpy_array(np.array([[0,1,0],[1,1,1],[0,0,0]]))

# nx.draw_spring(G, with_labels=True)
# plt.show()

