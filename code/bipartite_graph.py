import networkx
from networkx.algorithms import bipartite

# Create the actor/movie graph
g = networkx.Graph()
g.add_edges_from([("Stallone","Expendables"),("Schwarzenegger","Expendables")])
g.add_edges_from([("Schwarzenegger","Terminator 2"),("Furlong","Terminator 2")])
g.add_edges_from([("Furlong","Green Hornet"),("Diaz","Green Hornet")])

# Test if graph is bipartite
print bipartite.is_bipartite(g)
print bipartite.bipartite_sets(g)

# Graph is no longer bipartite after this
g.add_edge("Schwarzenegger","Stallone")
print bipartite.is_bipartite(g)
