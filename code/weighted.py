import networkx 

# Create a new graph
g = networkx.Graph()

# Add edges to the graph, with nodes added 'on the fly'
g.add_edge("conor@deri.org", "anne@ucd.ie", weight=5)
g.add_edge("conor@deri.org", "mark@yahoo.ie", weight=2)
g.add_edge("conor@deri.org", "maria@gmail.com", weight=4)
g.add_edge("mark@yahoo.ie", "maria@gmail.com", weight=3)

# Get strongly weighted edges above a threshold
estrong=[(u,v) for (u,v,d) in g.edges(data=True) if d["weight"] > 3]
print estrong

# Print weighted and unweighted degrees for all nodes in graph
print g.degree(weighted=False)
print g.degree(weighted=True)

# Print weighted and unweighted degrees for a specific node in graph
print g.degree("conor@deri.org", weighted=False)
print g.degree("conor@deri.org", weighted=True)
