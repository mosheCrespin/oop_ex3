import unittest
import time

from typing import List
from src.GraphAlgo import GraphAlgo
from src.network_x_graph import network_x
def intersection(l1, l2):
    return [value for value in l1 if value in l2]
def equal_lists(l1, l2):
    temp = len(l1)
    return len(intersection(l1, l2)) == temp
def equal_list_of_lists(l1: List[list], l2: List[list]):
    counter = 0
    if len(l1) != len(l2):
        return False
    for i in l1:
        for j in l2:
            if equal_lists(i, j):
                counter += 1
                break
    return counter == len(l1)

class MyTestCase(unittest.TestCase):

    def test_10_nodes_with_80_edges(self):
        file_name = "comapring_files/G_10_80_0.json"
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
        my_graph_connected_component = my_graph.connected_component(1)
        end = time.time()
        my_graph_connected_component_time = end - start

        # test for shortest path

        start = time.time()
        nx_shortest_path_len = nx.shortest_path_length(0, 8)
        nx_shortest_path_list = nx.shortest_path_list(0, 8)
        end = time.time()
        nx_shortest_path_time = end - start
        start = time.time()
        my_graph_shortest_path_len, my_graph_shortest_path_list = my_graph.shortest_path(0, 8)
        end = time.time()
        my_graph_shortest_path_time = end - start
        self.assertTrue(nx_shortest_path_len, my_graph_shortest_path_len)
        self.assertTrue(nx_shortest_path_list, my_graph_shortest_path_list)


        print("10_nodes_with_80_edges:")

        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path: {my_graph_shortest_path_time}")
        print(
            f"run time for networkX\n connected components: {scc_nx_time}, shortest path: {nx_shortest_path_time}")

        print(f"results: my graph:\n shortest path: {my_graph_shortest_path_len}\n connected component: {len(my_graph_connected_component)}\n connected components: {len(my_graph_scc)}")
        print("*"*10)
        print(f"results: networkX :\n shortest path: {nx_shortest_path_len}\n connected components: {len(nx_scc)}")

        print("-" * 50)



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
        my_graph_connected_component = my_graph.connected_component(3)
        end = time.time()
        my_graph_connected_component_time = end - start

        # test for shortest path

        start = time.time()
        nx_shortest_path_len = nx.shortest_path_length(12, 95)
        nx_shortest_path_list = nx.shortest_path_list(12, 95)
        end = time.time()
        nx_shortest_path_time = end - start
        start = time.time()
        my_graph_shortest_path_len, my_graph_shortest_path_list = my_graph.shortest_path(12, 95)
        end = time.time()
        my_graph_shortest_path_time = end - start
        self.assertTrue(nx_shortest_path_len, my_graph_shortest_path_len)
        self.assertTrue(nx_shortest_path_list, my_graph_shortest_path_list)

        print("100_nodes_with_800_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path: {my_graph_shortest_path_time}")
        print(
            f"run time for networkX\n connected components: {scc_nx_time}, shortest path: {nx_shortest_path_time}")

        print(
            f"results: my graph:\n shortest path: {my_graph_shortest_path_len}\n connected component: {len(my_graph_connected_component)}\n connected components: {len(my_graph_scc)}")
        print("*" * 10)
        print(f"results: networkX :\n shortest path: {nx_shortest_path_len}\n connected components: {len(nx_scc)}")

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
        my_graph_connected_component = my_graph.connected_component(430)
        end = time.time()
        my_graph_connected_component_time = end - start

        # test for shortest path

        start = time.time()
        nx_shortest_path_len = nx.shortest_path_length(10, 850)
        nx_shortest_path_list = nx.shortest_path_list(10, 850)
        end = time.time()
        nx_shortest_path_time = end - start
        start = time.time()
        my_graph_shortest_path_len, my_graph_shortest_path_list = my_graph.shortest_path(10, 850)
        end = time.time()
        my_graph_shortest_path_time = end - start
        self.assertTrue(nx_shortest_path_len, my_graph_shortest_path_len)
        self.assertTrue(nx_shortest_path_list, my_graph_shortest_path_list)


        print("1000_nodes_with_8000_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path: {my_graph_shortest_path_time}")
        print(
            f"run time for networkX\n connected components: {scc_nx_time}, shortest path: {nx_shortest_path_time}")

        print(
            f"results: my graph:\n shortest path: {my_graph_shortest_path_len}\n connected component: {len(my_graph_connected_component)}\n connected components: {len(my_graph_scc)}")
        print("*" * 10)
        print(f"results: networkX :\n shortest path: {nx_shortest_path_len}\n connected components: {len(nx_scc)}")
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
        my_graph_connected_component = my_graph.connected_component(1500)
        end = time.time()
        my_graph_connected_component_time = end - start

        # test for shortest path

        start = time.time()
        nx_shortest_path_len = nx.shortest_path_length(0, 9999)
        nx_shortest_path_list = nx.shortest_path_list(0, 9999)
        end = time.time()




        nx_shortest_path_time = end - start
        start = time.time()
        my_graph_shortest_path_len, my_graph_shortest_path_list = my_graph.shortest_path(0, 9999)
        end = time.time()





        my_graph_shortest_path_time = end - start
        self.assertTrue(nx_shortest_path_len, my_graph_shortest_path_len)
        self.assertTrue(nx_shortest_path_list, my_graph_shortest_path_list)

        print("10000_nodes_with_80000_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path: {my_graph_shortest_path_time}")
        print(
            f"run time for networkX\n connected components: {scc_nx_time}, shortest path: {nx_shortest_path_time}")

        print(
            f"results: my graph:\n shortest path: {my_graph_shortest_path_len}\n connected component: {len(my_graph_connected_component)}\n connected components: {len(my_graph_scc)}")
        print("*" * 10)
        print(f"results: networkX :\n shortest path: {nx_shortest_path_len}\n connected components: {len(nx_scc)}")

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
        my_graph_connected_component = my_graph.connected_component(600)
        end = time.time()
        my_graph_connected_component_time = end - start

        # test for shortest path

        start = time.time()
        nx_shortest_path_len = nx.shortest_path_length(0, 19999)
        nx_shortest_path_list = nx.shortest_path_list(0, 19999)
        end = time.time()
        nx_shortest_path_time = end - start
        start = time.time()
        my_graph_shortest_path_len, my_graph_shortest_path_list = my_graph.shortest_path(0, 19999)
        end = time.time()
        my_graph_shortest_path_time = end - start
        self.assertTrue(nx_shortest_path_len, my_graph_shortest_path_len)
        self.assertTrue(nx_shortest_path_list, my_graph_shortest_path_list)

        print("20000_nodes_with_160000_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path: {my_graph_shortest_path_time}")
        print(
            f"run time for networkX\n connected components: {scc_nx_time}, shortest path: {nx_shortest_path_time}")

        print(
            f"results: my graph:\n shortest path: {my_graph_shortest_path_len}\n connected component: {len(my_graph_connected_component)}\n connected components: {len(my_graph_scc)}")
        print("*" * 10)
        print(f"results: networkX :\n shortest path: {nx_shortest_path_len}\n connected components: {len(nx_scc)}")

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
        my_graph_connected_component = my_graph.connected_component(5000)
        end = time.time()
        my_graph_connected_component_time = end - start

        # test for shortest path

        start = time.time()
        nx_shortest_path_list = nx.shortest_path_list(0, 5000)
        end = time.time()
        nx_shortest_path_len = nx.shortest_path_length(0, 5000)  # just to be sure
        nx_shortest_path_time = end - start
        start = time.time()
        my_graph_shortest_path_len, my_graph_shortest_path_list = my_graph.shortest_path(0, 5000)
        end = time.time()
        my_graph_shortest_path_time = end - start
        self.assertTrue(nx_shortest_path_len, my_graph_shortest_path_len)
        self.assertTrue(nx_shortest_path_list, my_graph_shortest_path_list)


        print("30000_nodes_with_240000_edges:")
        print(
            f"run time for my graph\n connected component: {my_graph_connected_component_time}, connected components: {scc_my_graph_time}, shortest path: {my_graph_shortest_path_time}")
        print(
            f"run time for networkX\n connected components: {scc_nx_time}, shortest path: {nx_shortest_path_time}")

        print(
            f"results: my graph:\n shortest path: {my_graph_shortest_path_len}\n connected component: {len(my_graph_connected_component)}\n connected components: {len(my_graph_scc)}")
        print("*" * 10)
        print(f"results: networkX :\n shortest path: {nx_shortest_path_len}\n connected components: {len(nx_scc)}")

        print("-" * 50)


if __name__ == '__main__':
    unittest.main()
