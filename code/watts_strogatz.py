import networkx

# Number of nodes & neighbours
n = 50
k = 6

# Probability of rewiring
p = 0.3

# Generate the graph
g = networkx.watts_strogatz_graph(n, k, p)
networkx.write_edgelist(g, "watts_strogatz50.edgelist")

# We should have a low average shortest path length...
asp = networkx.average_shortest_path_length(g)
print asp
print "Average shortest path = %.3f" % asp
