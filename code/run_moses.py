import networkx

# Build a network
g = networkx.watts_strogatz_graph(60, 8, 0.3)
inpath= "test_moses.edgelist"
networkx.write_weighted_edgelist(g, inpath)

# Apply community finding
import subprocess
outpath="test_moses.comms"
# Note: replace path with location of the MOSES binary file
proc = subprocess.Popen(["/usr/bin/moses", inpath, outpath])
proc.wait()

# Parse the results
lines = open(outpath,"r").readlines()
print "Identified %d communities" % len(lines)
for i in range(len(lines)):
	print "Community", i
	print set(lines[i].strip().split(" "))
