from Node import Node
from Edge import Edge
from GeoLocation import GeoLocation
import GraphInterface
from DiGraph import DiGraph

pos1 = GeoLocation(10.2,5.4,0.0)
pos2 = GeoLocation(15.2,8.4,0.0)
pos3 = GeoLocation(12.0,1.2,0.0)
n1 = Node(pos1,0)
n2 = Node(pos2,1)
n3 = Node(pos3,2)

e1 = Edge(0,1,2.2)
e2 = Edge(0,2,1.2)
e3 = Edge(1,0,3.2)
e4 = Edge(1,2,4.5)

graph = DiGraph()
graph.add_node(0,(10.2,5.4,0.0))
graph.add_node(1,(15.2,8.4,0.0))
graph.add_node(2,(12.0,1.2,0.0))
graph.add_edge(0,1,2.2)
graph.add_edge(0,2,1.2)
graph.add_edge(1,0,3.2)
graph.add_edge(1,2,4.5)
print(graph.v_size())
print(graph.e_size())
print(graph.__repr__())
graph.remove_node(0)
print(graph.v_size())
print(graph.e_size())
print(graph.__repr__())
