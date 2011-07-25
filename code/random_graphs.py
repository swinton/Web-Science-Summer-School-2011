import networkx

# Generate erdos renyi random graph
g1 = networkx.erdos_renyi_graph(50, 0.05)
networkx.write_edgelist(g1, "erdos_renyi1.edgelist")

# Generate another erdos renyi random graph
g2 = networkx.erdos_renyi_graph(50, 0.3)
networkx.write_edgelist(g2, "erdos_renyi2.edgelist")

