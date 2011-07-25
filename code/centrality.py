import networkx
from operator import itemgetter

# Load test graph
g = networkx.read_edgelist("centrality.edgelist")
print g.nodes()

# Compute degree centrality
dc = networkx.degree_centrality(g)
# Re-order by score
print sorted(dc.items(), key=itemgetter(1), reverse=True)

# Compute betweenness centrality
bc = networkx.betweenness_centrality(g)
# Re-order by score
print sorted(bc.items(), key=itemgetter(1), reverse=True)

# Compute betweenness centrality
ec = networkx.eigenvector_centrality(g)
# Re-order by score
print sorted(ec.items(), key=itemgetter(1), reverse=True)