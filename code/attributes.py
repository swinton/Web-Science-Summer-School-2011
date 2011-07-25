import networkx
import datetime

# Create a new graph
g = networkx.Graph()

# Add nodes with attributes
g.add_node("318064061",screen_name="peter78",location="Galway",time_zone="GMT")
g.add_node("317756843",screen_name="mark763",location="London",time_zone="GMT")

# Add extra attributes
g.node["318064061"]["verified"] = False
g.node["317756843"]["verified"] = False

# Add edge with attributes
g.add_edge("318064061", "317756843", follow_date=datetime.datetime.now())

print g.nodes(data=True)
print g.edges()
