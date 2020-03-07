import networkx as nx
import matplotlib.pyplot as plt

colors = ['red', 'green', 'blue', 'yellow']
DG = nx.DiGraph()
DG.add_nodes_from(['A', 'B', 'C', 'D'])
DG.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('D','A')])
nx.draw(DG,with_labels=True, node_size=900, node_color = colors)
plt.show()