
import networkx as nx
import matplotlib.pyplot as plt

# Constructing graph from list of edges

G = nx.complete_graph(5)

print(nx.adjacency_matrix(G))

nx.draw_spring(G, with_labels=True)
plt.show()

nx.draw_planar(G, with_labels=True) # doesnt work for k=5 ---> not planar graph
plt.show()