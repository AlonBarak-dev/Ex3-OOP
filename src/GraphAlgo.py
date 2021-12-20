import traceback
from abc import ABC
from typing import List
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
            with open(file_name, 'r') as file:
                file.write(json.dumps(self.graph.to_dict()))
            return True
        except:
            traceback.print_exc()
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass
