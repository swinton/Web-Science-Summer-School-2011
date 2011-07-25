import networkx

# Create directed graph
g = networkx.DiGraph()
g.add_edges_from([("A","B"), ("C","A")])

# Calculate in and out degrees of all nodes, as maps
print g.in_degree(with_labels=True)
print g.out_degree(with_labels=True)

# Check neighbours of nodes
print g.neighbors("A")
print g.neighbors("B")
print g.successors("A")

# Convert to undirected graph
ug = g.to_undirected()
print ug.neighbors("B")
