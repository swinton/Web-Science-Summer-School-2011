import networkx 

# Create a new graph
g = networkx.Graph()

# Add some nodes
g.add_node("John")
g.add_node("Maria")
g.add_node("Alex")

# Add some edges beteween nodes
g.add_edge("John", "Alex")
g.add_edge("Maria", "Alex")

# Print details of graph
print g.number_of_nodes()
print g.number_of_edges()
print g.nodes()
print g.edges()

# Print degree of specific node and all nodes
print g.degree("John")
print g.degree()
