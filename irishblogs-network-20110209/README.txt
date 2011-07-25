Irish Blogosphere Network Data
Version: 2011-02-09
---------------------------------------------
This archive contains the network data used in the paper "Identifying Representative Textual Sources in Blog Networks". K. Wade, D. Greene, C. Lee, D. Archambault, P. Cunningham (2011)

For more details contact conradlee@gmail.com or visit http://mlg.ucd.ie/blogs

The archive contains two types of graph:
    * the post-link graph (weighted, directed)
    * the blogroll graph (unweighted, directed)
    
For your convenience, each graph is provided in four formats:
    * edgelist
        Each line has one directed edge in the form two tab-separated URLs. The first url is the source of the edge, the second is the target).  This format does not contain node attributes.
    * .net (pajek)
        Untested, not sure whether networkx exported this one correctly. This format does contain node attributes.
    * .gml 
        With node attributes.
    * .graphml
        With node attributes.
        
The node attributes are as follows:
    * post count: total number of posts by blog
    * category: from the irish blog index at www.irishblogdirectory.com, where available (only a minority of blogs have a value other than "unknown")
    * gce_comms: list of communities to which a node belongs according to the GCE community detection algorithm
    * moses_comm: list of communities to which a node belongs according to the MOSES community detection algorithm
    * infomap_comm: community to which a node belongs according to the infomap community detection algorithm
    
