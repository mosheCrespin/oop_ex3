from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
import GraphInterface
from typing import List
from queue import PriorityQueue as PQ


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = None):
        self.graph = g


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = 'inf'
        path_list = []

        if not self.graph.has_node(id1) or not self.graph.has_node(id2) or self.graph.all_out_edges_of_node(id2) is None:
            return (path, path_list)

        if id1.__eq__(id2):
            path = 0
            path_list.append(self)
            return (path, path_list)



    def dijkstra (self, start: int, dest: int):
        priority_qeueu = PQ()
        node_curr = self.graph.get_node(start)
        node_curr.set_prev(start)
        priority_qeueu.put(node_curr)

        while (priority_qeueu.not_empty and node_curr != dest):



