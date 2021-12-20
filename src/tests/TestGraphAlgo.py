from src.GraphAlgo import GraphAlgo
import unittest
import os


class TestGraphAlgo(unittest.TestCase):
    file_name = "../../data/A0.json"

    # def test_get_graph(self):
    #     graphAlgo = GraphAlgo()
    #     assert self.graphAlgo.get_graph() is not None, "returned None instead of graph"

    def test_load_from_json(self):
        graph_algo = GraphAlgo()
        assert graph_algo.load_from_json(self.file_name) is True, "load from json failed"
        assert graph_algo.get_graph().v_size() == 11, "load wasn't full"
        assert graph_algo.get_graph().e_size() == 22, "load wasn't full"

    def test_save_to_json(self):
        graph_algo = GraphAlgo()
        assert graph_algo.load_from_json(self.file_name) is True, "load from json failed"
        assert graph_algo.save_to_json("../../data/output0.json") is True, "The save process failed"
        #graph_algo2 = GraphAlgo()
        graph_algo.load_from_json("../../data/output0.json")
        assert graph_algo.get_graph().v_size() == 11, "save wasn't full"
        assert graph_algo.get_graph().e_size() == 22, "save wasn't full"
