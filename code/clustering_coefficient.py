import networkx

# Create graph
g = networkx.Graph()
g.add_edges_from([("a","b"),("b","c"),("b","d"),("c","d")])

# Get list of neighbours for a specific node
print networkx.neighbors(g, "b")

# Build a dictionary of local coefficient scores
print networkx.clustering(g, with_labels=True)

# Calculate global clustering coefficient score
ccs = networkx.clustering(g)
print ccs
print sum(ccs)/len(ccs)
