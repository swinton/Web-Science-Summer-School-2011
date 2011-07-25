import networkx 

# Read test graph
g = networkx.read_adjlist("test.adj")
print g.edges()

# Specify ego node
ego = "d"

# Create ego subgraph
nodes=set([ego]) 
nodes.update(g.neighbors(ego))
egonet = g.subgraph(nodes)

# Print details of ego subgraph
print egonet.nodes()
print egonet.edges()

