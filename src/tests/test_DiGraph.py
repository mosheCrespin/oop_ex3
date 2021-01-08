import unittest
from src.DiGraph import DiGraph


class TestStringMethods(unittest.TestCase):

    def test_add_node(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        self.assertEqual(10, g0.v_size())
        self.assertEqual(10, g0.get_mc())
        g0.add_node(9)  # added existed node
        self.assertEqual(10, g0.v_size())
        self.assertEqual(10, g0.get_mc())

    def test_add_edge(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        for i in range(0, 10):
            g0.add_edge(i, 9 - i, 0.2)
        self.assertFalse(g0.add_edge(3, 12, 2))  # added an edge between noedes that not exist
        self.assertEqual(10, g0.e_size())
        self.assertEqual(20, g0.get_mc())
        self.assertFalse(g0.add_edge(0, 9, 3))  # added exited edge
        self.assertEqual(10, g0.e_size())
        self.assertEqual(20, g0.get_mc())

    def test_remove_edge(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        for i in range(0, 10):
            g0.add_edge(i, 9 - i, 0.2)
        g0.remove_edge(0, 9)
        self.assertEqual(9, g0.e_size())
        self.assertEqual(21, g0.get_mc())

    def test_remove_node(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        g0.add_edge(4, 3, 1)
        g0.add_edge(4, 2, 1)
        g0.add_edge(2, 4, 1)
        g0.add_edge(1, 2, 1)
        g0.add_edge(5, 4, 1)
        g0.add_edge(2, 5, 1)
        g0.remove_node(4)
        self.assertEqual(g0.get_all_v().get(4), None)
        self.assertEqual(0, len(g0.all_out_edges_of_node(5)))
        self.assertEqual(9, g0.v_size())
        self.assertEqual(2, g0.e_size())

    def test_v_size(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        self.assertEqual(10, g0.v_size())

    def test_e_size(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        for i in range(0, 10):
            g0.add_edge(i, 9 - i, 0.2)
        self.assertEqual(10, g0.e_size())

    def test_get_all_v(self):
        g0 = DiGraph()
        flag = True
        for i in range(0, 10):
            g0.add_node(i)
        for i in range(0, 10):
            if i not in g0.get_all_v().keys(): flag = False
        self.assertTrue(flag)

    def test_all_in_edges_of_node(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        g0.add_edge(4, 3, 1)
        g0.add_edge(4, 2, 1)
        g0.add_edge(2, 4, 1)
        g0.add_edge(1, 2, 1)
        g0.add_edge(5, 3, 1)
        g0.add_edge(2, 5, 1)
        self.assertEqual(2, len(g0.all_in_edges_of_node(3)))
        g0.add_edge(1, 3, 1)
        self.assertEqual(3, len(g0.all_in_edges_of_node(3)))
        g0.add_edge(1, 3, 1)  # already existed
        self.assertEqual(3, len(g0.all_in_edges_of_node(3)))
        g0.remove_edge(1, 3)  # check if this dict updates after removing edge
        self.assertEqual(2, len(g0.all_in_edges_of_node(3)))

    def test_all_out_edges_of_node(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        g0.add_edge(4, 3, 1)
        g0.add_edge(4, 2, 1)
        g0.add_edge(2, 4, 1)
        g0.add_edge(1, 2, 1)
        g0.add_edge(5, 3, 1)
        g0.add_edge(4, 5, 1)
        temp = g0.all_out_edges_of_node(4)
        self.assertEqual(3, len(g0.all_out_edges_of_node(4)))
        g0.add_edge(4, 6, 1)
        self.assertEqual(4, len(g0.all_out_edges_of_node(4)))
        g0.add_edge(4, 6, 1)  # already existed
        self.assertEqual(4, len(g0.all_out_edges_of_node(4)))
        g0.remove_edge(4, 6)  # check if this dict updates after removing edge
        self.assertEqual(3, len(g0.all_out_edges_of_node(4)))

    def test_mc(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        g0.add_edge(4, 3, 1)
        g0.add_edge(4, 2, 1)
        g0.add_edge(2, 4, 1)
        g0.add_edge(1, 2, 1)
        g0.add_edge(5, 3, 1)
        g0.add_edge(4, 5, 1)
        self.assertEqual(16, g0.get_mc())
        g0.add_edge(4, 5, 1)  # already exist
        self.assertEqual(16, g0.get_mc())
        g0.add_node(3)  # already exist
        self.assertEqual(16, g0.get_mc())
        g0.remove_edge(2, 4)
        self.assertEqual(17, g0.get_mc())
        g0.remove_edge(2, 4)  # removing twice
        self.assertEqual(17, g0.get_mc())
        g0.remove_node(2)
        self.assertEqual(18, g0.get_mc())
        g0.remove_node(2)  # adding twice
        self.assertEqual(18, g0.get_mc())

    def test_get_weight(self):
        g0 = DiGraph()
        for i in range(0, 10):
            g0.add_node(i)
        g0.add_edge(4, 3, 1)
        g0.add_edge(4, 3, 0.5)  # should not update
        self.assertEqual(1, g0.get_weight(4, 3))
        self.assertEqual(-1, g0.get_weight(4, 5))  # there is no edge


if __name__ == '__main__':
    unittest.main()
