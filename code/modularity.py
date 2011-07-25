import networkx
import community

# Load standard "Karate club" graph
g = networkx.read_edgelist("karate.edgelist")
print "%d nodes, %d edges" % ( len(g.nodes()), len(g.edges()) )

# Apply Louvain algorithm
partition = community.best_partition( g )

# Print members of each community
for i in set(partition.values()):
	print "Community", i
	members = list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == i]
	print members
	

	

