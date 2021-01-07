import unittest

from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):



    def test_10_nodes_with_80_edges(self):
        file_name = "comapring_files/G_10_80_0.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        print(f" for graph with {graph.get_graph().v_size()} nodes, and {graph.get_graph().e_size()} edges there are: {len(graph.connected_components())} SCC")


    def test_100_nodes_with_800_edges(self):
        file_name = "comapring_files/G_100_800_0.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        print(f" for graph with {graph.get_graph().v_size()} nodes, and {graph.get_graph().e_size()} edges there are: {len(graph.connected_components())} SCC")

    def test_1000_nodes_with_8000_edges(self):
        file_name = "comapring_files/G_1000_8000_0.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        print(f" for graph with {graph.get_graph().v_size()} nodes, and {graph.get_graph().e_size()} edges there are: {len(graph.connected_components())} SCC")

    def test_10000_nodes_with_80000_edges(self):
        file_name = "comapring_files/G_10000_80000_0.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        print(f" for graph with {graph.get_graph().v_size()} nodes, and {graph.get_graph().e_size()} edges there are: {len(graph.connected_components())} SCC")

    def test_20000_nodes_with_160000_edges(self):
        file_name = "comapring_files/G_20000_160000_0.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        print(f" for graph with {graph.get_graph().v_size()} nodes, and {graph.get_graph().e_size()} edges there are: {len(graph.connected_components())} SCC")


    def test_30000_nodes_with_240000_edges(self):
        file_name = "comapring_files/G_30000_240000_0.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        print(len(graph.connected_components()))
        print(f" for graph with {graph.get_graph().v_size()} nodes, and {graph.get_graph().e_size()} edges there are: {len(graph.connected_components())} SCC")
