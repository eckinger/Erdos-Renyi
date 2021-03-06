import networkx as nx
import matplotlib.pyplot as plt

positions = dict(Albany = (-74, 43),
                 Boston = (-71, 42),
                 NYC = (-74, 41),
                 Philly = (-75, 40))

G = nx.DiGraph()

G.add_nodes_from(positions)

drive_times = {('Albany', 'Boston'): 3,
               ('Albany', 'NYC'): 4,
               ('Boston', 'NYC'): 4,
               ('NYC', 'Philly'): 2}

G.add_edges_from(drive_times)

nx.draw(G, positions,
        node_shape='s',
        node_size=2500,
        with_labels = True)

nx.draw_networkx_edge_labels(G, positions, edge_labels = drive_times)

plt.axis('equal')
plt.savefig('figs/chapter_2_02')
