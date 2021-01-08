import unittest
import time

from typing import List

from src.GraphAlgo import GraphAlgo
from src.network_x_graph import network_x

def intersection(l1, l2):
    return [value for value in l1 if value in l2]

def equal_lists(l1, l2):
    temp=len(l1)
    return len(intersection(l1,l2)) == temp

def equal_list_of_lists(l1 : List[list], l2: List[list]):
    counter=0
    if len(l1) != len(l2):
        return False
    for i in l1:
        for j in l2:
            if equal_lists(i,j):
                counter+=1
                break
    return counter==len(l1)


class MyTestCase(unittest.TestCase):

    def test_10_nodes_with_80_edges(self):
        file_name = "comapring_files/G_10_80_0.json"
        nx = network_x()
        nx.load_from_json(file_name)
        my_graph = GraphAlgo()
        my_graph.load_from_json(file_name)
        start=time.time()

        # test for connected copmponents

        nx_scc=nx.connected_components()
        end=time.time()
        scc_nx_time=end-start
        start=time.time()
        my_graph_scc=my_graph.connected_components()
        end=time.time()
        scc_my_graph_time=end-start
        self.assertTrue(equal_list_of_lists(nx_scc,my_graph_scc))


        # test for connected copmponent


        start = time.time()
        nx_connected_component = nx.connected_component(1)
        end = time.time()
        nx_connected_component_time = end - start
        start = time.time()
        my_graph_connected_component = my_graph.connected_component(1)
        end = time.time()
        my_graph_connected_component_time = end - start
        self.assertTrue(equal_lists(nx_connected_component,my_graph_connected_component))

        print("10_nodes_with_80_edges:")
        print(f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path--")
        print(f"run time for networkX\n connected component: {nx_connected_component_time}, connected components: {scc_nx_time}, shortest path--")
        print("-"*50)

    def test_100_nodes_with_800_edges(self):
        file_name = "comapring_files/G_100_800_0.json"
        nx = network_x()
        nx.load_from_json(file_name)
        my_graph = GraphAlgo()
        my_graph.load_from_json(file_name)
        start = time.time()

        # test for connected copmponents

        nx_scc = nx.connected_components()
        end = time.time()
        scc_nx_time = end - start
        start = time.time()
        my_graph_scc = my_graph.connected_components()
        end = time.time()
        scc_my_graph_time = end - start
        self.assertTrue(equal_list_of_lists(nx_scc, my_graph_scc))

        # test for connected copmponent

        start = time.time()
        nx_connected_component = nx.connected_component(1)
        end = time.time()
        nx_connected_component_time = end - start
        start = time.time()
        my_graph_connected_component = my_graph.connected_component(1)
        end = time.time()
        my_graph_connected_component_time = end - start
        self.assertTrue(equal_lists(nx_connected_component, my_graph_connected_component))

        print("100_nodes_with_800_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path--")
        print(
            f"run time for networkX\n connected component: {nx_connected_component_time}, connected components: {scc_nx_time}, shortest path--")
        print("-" * 50)

    def test_1000_nodes_with_8000_edges(self):
        file_name = "comapring_files/G_1000_8000_0.json"
        nx = network_x()
        nx.load_from_json(file_name)
        my_graph = GraphAlgo()
        my_graph.load_from_json(file_name)
        start = time.time()

        # test for connected copmponents

        nx_scc = nx.connected_components()
        end = time.time()
        scc_nx_time = end - start
        start = time.time()
        my_graph_scc = my_graph.connected_components()
        end = time.time()
        scc_my_graph_time = end - start
        self.assertTrue(equal_list_of_lists(nx_scc, my_graph_scc))

        # test for connected copmponent

        start = time.time()
        nx_connected_component = nx.connected_component(1)
        end = time.time()
        nx_connected_component_time = end - start
        start = time.time()
        my_graph_connected_component = my_graph.connected_component(1)
        end = time.time()
        my_graph_connected_component_time = end - start
        self.assertTrue(equal_lists(nx_connected_component, my_graph_connected_component))

        print("1000_nodes_with_8000_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path--")
        print(
            f"run time for networkX\n connected component: {nx_connected_component_time}, connected components: {scc_nx_time}, shortest path--")
        print("-" * 50)

    def test_10000_nodes_with_80000_edges(self):
        file_name = "comapring_files/G_10000_80000_0.json"
        nx = network_x()
        nx.load_from_json(file_name)
        my_graph = GraphAlgo()
        my_graph.load_from_json(file_name)
        start = time.time()

        # test for connected copmponents

        nx_scc = nx.connected_components()
        end = time.time()
        scc_nx_time = end - start
        start = time.time()
        my_graph_scc = my_graph.connected_components()
        end = time.time()
        scc_my_graph_time = end - start
        self.assertTrue(equal_list_of_lists(nx_scc, my_graph_scc))

        # test for connected copmponent

        start = time.time()
        nx_connected_component = nx.connected_component(1)
        end = time.time()
        nx_connected_component_time = end - start
        start = time.time()
        my_graph_connected_component = my_graph.connected_component(1)
        end = time.time()
        my_graph_connected_component_time = end - start
        self.assertTrue(equal_lists(nx_connected_component, my_graph_connected_component))

        print("10000_nodes_with_80000_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path--")
        print(
            f"run time for networkX\n connected component: {nx_connected_component_time}, connected components: {scc_nx_time}, shortest path--")
        print("-" * 50)

    def test_20000_nodes_with_160000_edges(self):
        file_name = "comapring_files/G_20000_160000_0.json"
        nx = network_x()
        nx.load_from_json(file_name)
        my_graph = GraphAlgo()
        my_graph.load_from_json(file_name)
        start = time.time()

        # test for connected copmponents

        nx_scc = nx.connected_components()
        end = time.time()
        scc_nx_time = end - start
        start = time.time()
        my_graph_scc = my_graph.connected_components()
        end = time.time()
        scc_my_graph_time = end - start
        self.assertTrue(equal_list_of_lists(nx_scc, my_graph_scc))

        # test for connected copmponent

        start = time.time()
        nx_connected_component = nx.connected_component(1)
        end = time.time()
        nx_connected_component_time = end - start
        start = time.time()
        my_graph_connected_component = my_graph.connected_component(1)
        end = time.time()
        my_graph_connected_component_time = end - start
        self.assertTrue(equal_lists(nx_connected_component, my_graph_connected_component))

        print("20000_nodes_with_160000_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path--")
        print(
            f"run time for networkX\n connected component: {nx_connected_component_time}, connected components: {scc_nx_time}, shortest path--")
        print("-" * 50)


    def test_30000_nodes_with_240000_edges(self):
        file_name = "comapring_files/G_30000_240000_0.json"
        nx = network_x()
        nx.load_from_json(file_name)
        my_graph = GraphAlgo()
        my_graph.load_from_json(file_name)
        start = time.time()

        # test for connected copmponents

        nx_scc = nx.connected_components()
        end = time.time()
        scc_nx_time = end - start
        start = time.time()
        my_graph_scc = my_graph.connected_components()
        end = time.time()
        scc_my_graph_time = end - start
        self.assertTrue(equal_list_of_lists(nx_scc, my_graph_scc))

        # test for connected copmponent

        start = time.time()
        nx_connected_component = nx.connected_component(1)
        end = time.time()
        nx_connected_component_time = end - start
        start = time.time()
        my_graph_connected_component = my_graph.connected_component(1)
        end = time.time()
        my_graph_connected_component_time = end - start
        self.assertTrue(equal_lists(nx_connected_component, my_graph_connected_component))

        print("30000_nodes_with_240000_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path--")
        print(
            f"run time for networkX\n connected component: {nx_connected_component_time}, connected components: {scc_nx_time}, shortest path--")
        print("-" * 50)

if __name__ == '__main__':
    unittest.main()
