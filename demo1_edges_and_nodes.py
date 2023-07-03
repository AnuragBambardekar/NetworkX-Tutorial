# pip install networkx

import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph() # a simple undirected graph
# G = nx.DiGraph() # directed graph
# G = nx.MultiGraph() # graph with edges, name, or graph attributes.
# G = nx.MultiDiGraph()

G.add_edge(1,2) # Add an edge between 1st node, 2nd node
G.add_edge(2,3,weight=0.9)

G.add_edge("A","B")
G.add_edge("B","B")
G.add_node("C")

G.add_node(print)

# Adding attributes to Nodes
for i in G.nodes:
    G.nodes[i]['Cyclist'] = False
    G.nodes[i]['weight'] = random.choice(range(100,200))

G.nodes[1]['cyclist'] = True

print(G.nodes)
print(G.nodes.data())
print(G.edges)
print(G.degree)
print(G.adj)
print(G.number_of_edges())
print(G.number_of_nodes())

nx.draw_spring(G, with_labels=True)
plt.show()

