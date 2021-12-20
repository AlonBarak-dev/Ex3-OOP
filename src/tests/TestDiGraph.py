import unittest
from src.GeoLocation import GeoLocation
from src.Node import Node
from src.Edge import Edge
from src.DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):
    # init graph
    graph = DiGraph()
    # init GeoLocation
    p1 = GeoLocation(0.0,0.0,0.0)
    # init Nodes
    node0 = Node(p1,0)
    node1 = Node(key=1)     #no position
    node2 = Node(p1,2)
    node3 = Node(p1,3)
    node4 = Node(key=4)     # no position
    # init Edges
    edge01 = Edge(0,1,5.0)
    edge04 = Edge(0,4,4.2)
    edge23 = Edge(2,3,8)
    edge31 = Edge(3,1,0.5)
    edge24 = Edge(2,4,1)

    def build_graph(self):
        self.graph.add_node2(self.node0)
        self.graph.add_node2(self.node1)
        self.graph.add_node2(self.node2)
        self.graph.add_node2(self.node3)
        self.graph.add_node2(self.node4)
        self.graph.add_edge2(self.edge01)
        self.graph.add_edge2(self.edge04)
        self.graph.add_edge2(self.edge23)
        self.graph.add_edge2(self.edge31)
        self.graph.add_edge2(self.edge24)


    def test_v_size(self):
        self.build_graph()
        size = self.graph.v_size()
        assert size == 5, "wrong vertex size"
        self.graph.remove_node(0)
        size = self.graph.v_size()
        assert size == 4, "should've changed to 4"




    # def test_e_size(self):
    #
    # def test_get_all_v(self):
    #
    # def test_all_in_edges_of_node(self):
    #
    # def test_all_out_edges_of_node(self):
    #
    # def test_get_mc(self):
    #
    # def test_add_edge(self):
    #
    # def test_add_node(self):
    #
    # def test_remove_edge(self):
    #
    # def test_remove_node(self):
