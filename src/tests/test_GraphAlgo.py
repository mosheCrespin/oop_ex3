import random
import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_shortest_path(self):
        g = DiGraph()
        for i in range(0, 5):
            g.add_node(i)
        i = 0
        g.add_edge(0, 1, 10)
        g.add_edge(1, 2, 10)
        g.add_edge(0, 2, 5)
        g.add_edge(2, 3, 10)
        g.add_edge(3, 4, 10)

        graph = GraphAlgo(g)
        (path, path_list) = (25, [0, 2, 3, 4])
        (p, pl) = graph.shortest_path(0, 4)
        self.assertEqual(path, p)
        self.assertEqual(path_list, pl)

        (path0, path_list0) = (float('inf'), [])
        (p0, pl0) = graph.shortest_path(4, 0)
        self.assertEqual(path0, p0)
        self.assertEqual(path_list0, pl0)

    def test_connected_component(self):
        g = DiGraph()
        for i in range(1, 8):
            g.add_node(i)
        g.add_edge(1, 2, 10)
        g.add_edge(2, 1, 10)
        g.add_edge(1, 3, 10)
        g.add_edge(3, 1, 10)
        g.add_edge(2, 4, 10)
        g.add_edge(3, 4, 10)
        g.add_edge(1, 7, 10)
        g.add_edge(7, 5, 10)
        g.add_edge(5, 7, 10)
        g.add_edge(7, 6, 10)
        g.add_edge(6, 7, 10)
        graph = GraphAlgo(g)
        x, y, z = graph.connected_component(1)
        self.assertEqual(1, x)
        self.assertEqual(2, y)
        self.assertEqual(3, z)
        self.assertEqual(0, len(graph.connected_component(13)))  # not exists node

    def test_connected_components(self):
        g=DiGraph()
        graph = GraphAlgo(g)
        # file_name="to moshe with love.json"
        # graph.load_from_json(file_name)
        # print(len(graph.connected_components()))

        self.assertEqual(0, len(graph.connected_components()))  # there is no nodes
        for i in range(1, 8):
            g.add_node(i)
        ll = graph.connected_components()
        self.assertEqual(7, len(ll))
        for i in range(1, 8):
            self.assertEqual(ll[i - 1][0], i)  # graph without edges
        g.add_edge(1, 2, 10)
        g.add_edge(2, 1, 10)
        g.add_edge(1, 3, 1)
        g.add_edge(3, 1, 10)
        g.add_edge(2, 4, 10)
        g.add_edge(1, 7, 10)
        g.add_edge(7, 5, 10)
        g.add_edge(5, 7, 10)
        g.add_edge(7, 6, 10)
        g.add_edge(6, 7, 10)
        self.assertEqual(3, len(graph.connected_components()))
        print(graph.connected_components())
        graph.plot_graph()

    def test_plot(self):
        file_name = "A0.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        graph.plot_graph()
        file_name = "T0.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        graph.plot_graph()
        file_name = "A2.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        graph.plot_graph()
        file_name = "A3.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        graph.plot_graph()
        file_name = "A4.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        graph.plot_graph()
        file_name = "A5_edited.json"
        graph = GraphAlgo()
        graph.load_from_json(file_name)
        graph.plot_graph()
        g = DiGraph()
        for i in range(1, 8):
            g.add_node(i)
        g.add_edge(1, 2, 10)
        g.add_edge(2, 1, 10)
        g.add_edge(1, 3, 10)
        g.add_edge(3, 1, 10)
        g.add_edge(2, 4, 10)
        g.add_edge(3, 4, 10)
        g.add_edge(1, 7, 10)
        g.add_edge(7, 5, 10)
        g.add_edge(5, 7, 10)
        g.add_edge(7, 6, 10)
        g.add_edge(6, 7, 10)
        graph = GraphAlgo(g)
        graph.plot_graph()

    def test_save_to_json(self):
        g = DiGraph()
        for i in range(1, 8):
            g.add_node(i)
        g.add_edge(1, 2, 10)
        g.add_edge(2, 1, 10)
        g.add_edge(1, 3, 10)
        g.add_edge(3, 1, 10)
        g.add_edge(2, 4, 10)
        g.add_edge(3, 4, 10)
        g.add_edge(1, 7, 10)
        g.add_edge(7, 5, 10)
        g.add_edge(5, 7, 10)
        g.add_edge(7, 6, 10)
        g.add_edge(6, 7, 10)
        graph = GraphAlgo(g)
        file = "test4.json"
        graph.save_to_json(file)

        def million_graph_creator(self):
            graph = DiGraph()
            for i in range(1, 1000001):
                graph.add_node(i)
            for i in range(1, 1000001):
                for j in (i, i + 10):
                    x = random.randint(1, 1000000)
                    graph.add_edge(i, x, weight=1)
            return graph

    def test_load_from_json(self):
        file_name = "to moshe with love.json"
        graph = DiGraph()
        # graph.load_from_json(file_name)

        # def million_graph_creator(self):
        #     graph = DiGraph()
        for i in range(1, 1000001):
            graph.add_node(i)
        for i in range(1, 1000001):
            for j in (i, i + 10):
                x = random.randint(1, 1000000)
                graph.add_edge(i, x, 1)
        ga=GraphAlgo(graph)
        print(ga.get_graph().number_of_edges)
        print(ga.get_graph().number_of_nodes)
        print(len(ga.connected_components()))




if __name__ == '__main__':
    unittest.main()
