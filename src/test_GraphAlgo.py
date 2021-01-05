import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

class MyTestCase(unittest.TestCase):
    def test_shortest_path(self):
        g = DiGraph()
        for i in range(0,5):
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
        g.add_edge(1, 3, 1)
        g.add_edge(2, 4, 10)
        g.add_edge(1, 7, 10)
        g.add_edge(7, 5, 10)
        g.add_edge(5, 7, 10)
        g.add_edge(7, 6, 10)
        g.add_edge(6, 7, 10)
        graph = GraphAlgo(g)
        (p,pl) = graph.shortest_path(1, 7)
        print(graph.shortest_path(4, 1))

if __name__ == '__main__':
    unittest.main()
