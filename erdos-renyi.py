import networkx as nx
import matplotlib.pyplot as plt

# an undirected graph is *connected* if there is a path from every node to every other node

# generate a complete graph
    # complete graph: where every node is connected to every other

def all_pairs(nodes):
    for i, u in enumerate(nodes):
        for j, v in enumerate(nodes):
            if i < j:
                yield u, v

def make_complete_graph(n):
    G = nx.Graph()
    nodes = range(n)
    G.add_nodes_from(nodes)
    G.add_edges_from(all_pairs(nodes))
    return G

complete = make_complete_graph(10)
nx.draw_circular(complete,
                 node_size = 1000,
                 with_labels = True)
plt.axis('equal')
plt.savefig('figs/chapter_2_03')

