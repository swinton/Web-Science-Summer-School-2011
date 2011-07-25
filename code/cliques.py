import networkx

# Load test graph
g = networkx.read_edgelist("cliques.edgelist")
print g.nodes()

# Find all maximal cliques
cl = list( networkx.find_cliques(g) )
print cl
