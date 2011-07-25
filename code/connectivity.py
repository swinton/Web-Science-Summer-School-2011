import networkx

# Create graph
g = networkx.Graph()
g.add_edges_from([("a","b"),("b","c"),("b","d"),("c","d")])
g.add_edges_from([("e","f"),("f","g"),("h","i")])

# Is the graph just a single connected component?
print networkx.is_connected(g)

# How many components?
print networkx.number_connected_components(g)

# Find content of connected components in the graph
comps = networkx.connected_component_subgraphs(g)
print comps[0].nodes()
print comps[1].nodes()
print comps[2].nodes()