# how centrally positioned is a node in a graph
# so, higher the degree of a node, higher the centrality --> this is one way to determine centrality
# there is also closeness centrality, eigen centrality (which takes into account quality of nodes), 
# betweenness centrality (important paths that run through a node)

import networkx as nx
import matplotlib.pyplot as plt

# edge_list = [(1,2),(2,3),(3,4),(4,5),(3,6),(6,7),(2,8),(8,9),(9,4)]

# G = nx.Graph()
# G.add_edges_from(edge_list)

# print(nx.degree_centrality(G))
# print(nx.closeness_centrality(G))
# print(nx.eigenvector_centrality(G))
# print(nx.betweenness_centrality(G))

# nx.draw_planar(G, with_labels=True)
# plt.show()

G1 = nx.complete_graph(5)
G2 = nx.complete_graph(5)
G2 = nx.relabel_nodes(G2, {0:"a",1:"b",2:"c",3:"d",4:"e"})
G_connector = nx.from_edgelist([(4,'x'), ('x','a')])
G = nx.compose_all([G1,G2, G_connector])

print(nx.degree_centrality(G))
print(nx.betweenness_centrality(G)) # x is important

print(nx.density(G)) # The density is 0 for a graph without edges and 1 for a complete graph. 
print(nx.diameter(G)) # longest - shortest path

nx.draw_spring(G, with_labels=True)
plt.show()


