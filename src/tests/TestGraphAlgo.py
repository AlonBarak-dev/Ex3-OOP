from src.GraphAlgo import GraphAlgo
import unittest
import os


class TestGraphAlgo(unittest.TestCase):
    file_name = "../../data/A0.json"
    graph = GraphAlgo()

    def test_load_from_json(self):
        print(os.getcwd())
        assert self.graph.load_from_json(self.file_name) is True, "load from json failed"
        assert self.graph.graph.v_size() == 11, "load wasn't full"
        assert self.graph.graph.e_size() == 22, "load wasn't full"

