import networkx 

# Read graph in adjacency list format
g = networkx.read_adjlist("test.adj")
print g.edges()

# Read graph in edge list format
g = networkx.read_edgelist("test.edgelist")
print g.edges()