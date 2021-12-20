import traceback
from _heapq import heappop
from abc import ABC
from heapq import heappush
from typing import List, Dict
from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.Edge import Edge
from src.Node import Node
from src.GeoLocation import GeoLocation
from src.DiGraph import DiGraph
import json


class GraphAlgo(GraphAlgoInterface):
    """
    This class implement the abstract class GraphAlgoInterface from src Directory.
    It allows the User to run different algorithms on the Graph
    """

    def __init__(self):
        self.graph: DiGraph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        self.graph = DiGraph()
        try:  # loading the json file
            with open(file_name, 'r') as file:
                data = json.loads(file.read())

            nodes = data.get("Nodes")  # the nodes dict
            edges = data.get("Edges")  # the edges dict

            for node in nodes:
                new_node: Node = Node.from_dict(node)  # creating new nodes from the dict
                self.graph.add_node2(new_node)  # adding to the graph

            for edge in edges:
                new_edge: Edge = Edge.from_dict(edge)  # creating new edges from the dict
                self.graph.add_edge2(new_edge)  # adding the edges to the graph

            return True

        except:
            traceback.print_exc()
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, 'w+') as file:
                file.write(json.dumps(self.graph.to_dict()))
            return True
        except:
            traceback.print_exc()
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        """
        self.reset_tags()       # reset all tags to 0 -> NOT VISITED

        source = id1
        destination = id2
        deltas: Dict[int, float] = {}       # represent the 2D array of distances in dijkstra algorithm
        priority_q: [] = []     # a list representing the priority Queue we used in EX2

        total_dist = -1     # init the return dist
        path = []

        # in case one of the nodes is not in the graph
        if id1 not in self.graph.nodes or id2 not in self.graph.nodes:
            result = (total_dist, path)  # default tuple
            return result

        heappush(priority_q, (0.0, self.get_graph().get_all_v().get(source)))
        deltas[source] = 0.0

        dest_node: Node = None

        while len(priority_q) > 0:

            node_distance, node = heappop(priority_q)   # Extract node with minimum delta(dist) and its delta

            node.tag = 1
            if node.key == destination:
                dest_node = node

            # iterate over the neighbors of node (out edges)
            for ngbr_id, ngbr_w in self.get_graph().all_out_edges_of_node(node.key).items():

                neighbour: Node = self.get_graph().get_all_v().get(ngbr_id)     # neighbor node

                if neighbour.tag == 1:  # if the node already visited, skip him
                    continue

                new_neighbour_delta = deltas.get(node.key) + ngbr_w      # calculating the new delta

                # relaxing the path >> found more efficient way
                if new_neighbour_delta < deltas.get(ngbr_id, float("inf")):
                    heappush(priority_q, (new_neighbour_delta, neighbour))
                    deltas[ngbr_id] = new_neighbour_delta
                    neighbour.tag = 2       # node is queued
                    neighbour.info = "{}".format(node.key)      # update the info so it contain its parent key so we
                                                                # can track the path after we done

        if dest_node is not None:       # Reached the desired Node (there is a path)
            total_dist = deltas.get(destination)
            path = self.__backtrack_path(source, dest_node)

        # Reset tags back to 0 when finished
        self.reset_tags()

        result = (total_dist, path)     # the result tuple with its new data (the total distance of the path, the path)
        return result

    def __backtrack_path(self, src: int, dest_node: Node) -> List[Node]:
        """
        create a path for shortest path.
        :param src: source Node.
        :param dest_node: Destination Node.
        :return: list of nodes
        """
        path: List = []     # A list which will contain the nodes in the shortest path

        child: Node = dest_node     # the last child in our path

        while child.key != src:     # DO SO until first parent is reached(src node)

            path.insert(0, child.key)
            if child.info:      # has parent?
                child = self.get_graph().get_all_v().get(int(child.info))       # update child to its father

        path.insert(0, child.key)       # insert the src node as well

        return path

    def reset_tags(self):
        """
        This method reset all the graph's Node's tags to 0 -> NOT VISITED YET
        """
        for n in self.get_graph().get_all_v().values():
            n.tag = 0       # NOT VISITED YET











    def plot_graph(self) -> None:
        pass
