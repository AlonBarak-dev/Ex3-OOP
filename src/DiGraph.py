import json

from src.GraphInterface import GraphInterface
from Edge import Edge
from Links import Links
from Node import Node
from GeoLocation import GeoLocation


class DiGraph(GraphInterface):

    def __init__(self):
        """
        empty constructor for DiGraph class
        """
        self.mode_count = 0
        self.edges = {}
        self.nodes = {}

    # def from_json(self,file:str):
    #
    #     with open(file,'r') as f:
    #         data = json.load(f)     # importing the json file into a dict
    #

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """

        return len(self.edges)

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph, each node is represented using a pair
        (node_id, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
        """
        output = {}  # new dict
        for edge in self.nodes[id1].edges_in.values():  # iterate over the edges coming into the given node
            output[edge.src] = edge.weight  # (other_node_id, weight)
        return output

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        output = {}  # new dict
        for edge in self.nodes[id1].edges_out.values():
            output[edge.dest] = edge.weight
        return output

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mode_count

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

        # check whether the given nodes are in the graph or not.
        if id1 not in self.nodes or id2 not in self.nodes:
            return False
        # check whether the given edge already exists in the Graph or not
        if id1 in self.edges:
            if id2 in self.edges[id1]:
                return False

        edge = Edge(id1,id2,weight)     # create a new Edge from the given data
        self.edges[id1][id2] = edge     # add the edge to the dict
        self.nodes[id1].edges_out[id2] = edge
        self.nodes[id2].edges_in[id1] = edge
        self.mode_count += 1        # update mode counter
        return True



    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """

        # check whether the node already exists in the Graph or not
        if node_id in self.nodes:
            return False

        # creates a new Node
        x = pos[0]
        y = pos[1]
        z = pos[2]
        pos = GeoLocation(x,y,z)
        node = Node(pos,node_id)
        # adds the new node to the Graph
        self.nodes[node_id] = node
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """

        # check whether the given nodes exists in the Graph or not
        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            return False
        # check whether the given edge exists in the graph or not
        if node_id2 not in self.edges[node_id1]:
            return False

        # removes the edge from graph
        del self.edges[node_id1][node_id2]
        # removes all the edges that getting out of the node
        del self.nodes[node_id1].edges_out[node_id2]
        # removes all the edges that getting into the node
        del self.nodes[node_id2].edges_in[node_id1]

        self.mode_count += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
       Removes a node from the graph.
       @param node_id: The node ID
       @return: True if the node was removed successfully, False o.w.
       Note: if the node id does not exists the function will do nothing
       """
        # checks whether the particular node exists or not
        if node_id not in self.nodes:
            return False


        for node in self.nodes:
            # removes all the edges that getting into the node
            del node.edges_in[node_id]
            # removes all the edges that getting out of the node
            del node.edges_out[node_id]

        for edge in self.edges:
            # removes all the edges that contains the node (whether as source or dest)
            if edge.src == node_id or edge.dest == node_id:
                del edge

        # deletes the particular node from the Graph
        del self.nodes[node_id]

        self.mode_count += 1

        return True




