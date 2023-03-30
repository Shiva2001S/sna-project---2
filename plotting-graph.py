import networkx as nx
import matplotlib.pyplot as plt

# Load data as a NetworkX graph
G = nx.read_edgelist('predicted_links.csv', delimiter=',')

# Draw the graph
nx.draw(G, with_labels=True)
plt.show()
