import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node('Alina')
G.add_node('Ben')
G.add_node('Eshan')

print('List of nodes: ' + str(list(G.nodes())))

G.add_edge('Alina', 'Ben')
G.add_edge('Alina', 'Eshan')
G.add_edge('Ben', 'Alina')
G.add_edge('Ben', 'Eshan')

print('List of edges: ' + str(list(G.edges())))

nx.draw_circular(G,
                 node_size = 2000,
                 with_labels = True)

plt.axis('equal')
plt.savefig('figs/chapter_2_01')
