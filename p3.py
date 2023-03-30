import itertools
import networkx as nx

# Load data as a NetworkX graph
G = nx.read_edgelist('my3.csv', delimiter=',')

# Compute betweenness centrality for all nodes
bc = nx.betweenness_centrality(G)

# Compute closeness centrality for all nodes
cc = nx.closeness_centrality(G)

# Set a threshold value
threshold = 0.5

# Iterate over all pairs of nodes and predict links based on high betweenness and closeness centrality
for u, v in itertools.combinations(G.nodes(), 2):
    if not G.has_edge(u, v) and bc[u] + bc[v] + cc[u] + cc[v] > threshold:
        G.add_edge(u, v)

# Save predicted links to a new file
nx.write_edgelist(G, 'predicted_links.csv', delimiter=',')
