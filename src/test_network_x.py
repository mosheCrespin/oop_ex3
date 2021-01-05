import unittest
from src.network_x_graph import network_x

file = "test20.json"


class MyTestCase(unittest.TestCase):
    def test_draw_nodes(self):
        nx = network_x()
        graph = network_x().graph
        nx.load_from_json(file)
        nx.draw_graph()
    def test_shortest_path(self):
        nx=network_x()
        graph=network_x().graph
        nx.load_from_json(file)
        print(nx.shortest_path(2,5))


        print(type(graph))
    def test_connected_components(self):
        nx = network_x()
        nx.load_from_json(file)
        nx.connected_componnets()


if __name__ == '__main__':
    unittest.main()
