from src import DiGraph, GraphInterface
from src.GraphAlgo import GraphAlgo
import unittest
import os


class TestGraphAlgo(unittest.TestCase):
    file_name = "../../data/A0.json"

    def test_load_from_json(self):
        graph_algo = GraphAlgo()
        assert graph_algo.load_from_json(self.file_name) is True, "load from json failed"
        assert graph_algo.get_graph().v_size() == 11, "load wasn't full"
        assert graph_algo.get_graph().e_size() == 22, "load wasn't full"

    def test_save_to_json(self):
        graph_algo = GraphAlgo()
        assert graph_algo.load_from_json(self.file_name) is True, "load from json failed"
        assert graph_algo.save_to_json("../../data/output0.json") is True, "The save process failed"
        graph_algo.load_from_json("../../data/output0.json")
        assert graph_algo.get_graph().v_size() == 11, "save wasn't full"
        assert graph_algo.get_graph().e_size() == 22, "save wasn't full"

    def test_get_graph(self):
        graph_algo = GraphAlgo()
        assert graph_algo.get_graph().mode_count == 0, "returned graph instead of None"
        if graph_algo.load_from_json(self.file_name) is True:
            assert isinstance(graph_algo.get_graph(), GraphInterface.GraphInterface), "returned graph instead of None"

    def test_shortest_path(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json(self.file_name)

        dist, path = graph_algo.shortest_path(0, 7)
        # print(path)
        self.assertEqual(dist, 5.653293226161572)
        self.assertEqual([0, 10, 9, 8, 7], path)

        dist, path = graph_algo.shortest_path(0, 8888887)
        # print(path)
        self.assertEqual(dist, -1)
        self.assertEqual(path, [])

    def test_TSP(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("../../data/A0.json")

        path, dist = graph_algo.TSP([0, 1, 2, 3, 4, 7])
        self.assertEqual(dist, 10.240617338114607)
        self.assertEqual(path, [0, 1, 2, 3, 4, 5, 6, 7])

        graph_algo.load_from_json("../../data/A4.json")
        path, dist = graph_algo.TSP([0, 1, 5, 3, 4, 12])
        self.assertEqual(dist, 14.598487672362879)
        self.assertEqual(path, [0, 1, 2, 3, 4, 5, 6, 15, 14, 13, 12])

        # print(path)
        # print(dist)
