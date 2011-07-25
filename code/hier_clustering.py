import networkx
import numpy
import matplotlib
from scipy.cluster import hierarchy
from scipy.spatial import distance

# Load standard "Karate club" graph
g = networkx.read_edgelist("karate.edgelist")
print "%d nodes, %d edges" % ( len(g.nodes()), len(g.edges()) )

# Build a distance matrix, based on shortest paths
path_length=networkx.all_pairs_shortest_path_length(g)
n = len(g.nodes())
distances=numpy.zeros((n,n))
for u,p in path_length.iteritems():
	for v,d in p.iteritems():
		distances[int(u)-1][int(v)-1] = d
		
# Apply average-linkage agglomerative clustering
Y = distance.squareform(distances)
Z = hierarchy.average(Y)		

# Generate the tree and save it to disk
hierarchy.dendrogram(Z)
matplotlib.pylab.savefig("tree.png", format="png")
