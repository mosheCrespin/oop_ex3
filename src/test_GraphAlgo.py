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
        g.add_edge(2, 3, 10)
        g.add_edge(3, 4, 10)

        graph = GraphAlgo(g)
        (path, path_list) = (40, [0, 1, 2, 3, 4])
        (p, pl) = graph.shortest_path(0, 4)
        self.assertEqual(path, p)
        self.assertEqual(path_list, pl)



if __name__ == '__main__':
    unittest.main()
