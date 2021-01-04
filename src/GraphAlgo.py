from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import GraphInterface
from queue import PriorityQueue as PQ
import copy
import collections
from typing import List
import json


def intersection(l1, l2):
    return [value for value in l1 if value in l2]


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = None):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def connected_component(self, id1: int) -> list:
        list_component = []
        for i in self.graph.get_all_v().keys():
            w, p = self.shortest_path(id1, i)
            if w != float('inf') and len(p) != 0:
                list_component.append(i)
        deep_copied_graph = copy.deepcopy(self.graph)
        temp = deep_copied_graph.get_out_edges()
        deep_copied_graph.set_out_edges(deep_copied_graph.in_edges)
        deep_copied_graph.set_in_edges(temp)
        temp_graph = self.graph
        self.graph = deep_copied_graph
        temporary_list = []
        for i in deep_copied_graph.get_all_v().keys():
            w, p = self.shortest_path(id1, i)
            if w != float('inf') and len(p) != 0:
                temporary_list.append(i)
        self.graph = temp_graph
        return intersection(list_component, temporary_list)

    def connected_components(self) -> List[list]:
        ans = []
        for i in self.graph.get_all_v():
            temp = sorted(self.connected_component(i))
            if temp not in ans:
                ans.append(temp)
        return ans

    def plot_graph(self) -> None:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = float('inf')
        path_list = []

        if not self.graph.has_node(id1) or not self.graph.has_node(id2):
            return (path, path_list)

        if id1 == id2:
            path = 0
            path_list.append(self)
            return (path, path_list)

        self.reset_prevAndDist()
        self.dijkstra(id1, id2)

        path = self.graph.get_node(id2).distance

        if (path != -1):

            path_list.insert(0, id2)
            node_prev = self.graph.get_node(id2).prev

            while (node_prev != id1):
                path_list.insert(0, node_prev)
                node_prev = self.graph.get_node(node_prev).prev
            path_list.insert(0, id1)
        else:
            path = float('inf')

        return (path, path_list)

    def dijkstra(self, start: int, dest: int):
        priority_qeueu = PQ()
        node_curr = self.graph.get_node(start)
        node_curr.set_prev(start)
        node_curr.set_distance(0)
        priority_qeueu.put(node_curr)

        while (priority_qeueu.qsize() != 0 and node_curr.id() != dest):

            node_curr = priority_qeueu.get()

            for key in self.graph.all_out_edges_of_node(node_curr.id()).keys():
                node_na = self.graph.get_node(key)
                edge_weight = self.graph.get_weight(node_curr.id(), key)

                if (node_na.prev == -1):
                    node_na.set_prev(node_curr.id())
                    node_na.set_distance(node_curr.distance + edge_weight)
                    priority_qeueu.put(node_na)

                elif (node_na.distance > node_curr.distance + edge_weight):
                    node_na.set_prev(node_curr.id())
                    node_na.set_distance(node_curr.distance + edge_weight)

    def reset_prevAndDist(self):
        for node in self.graph.my_graph.values():
            node.set_prev(-1)
            node.set_distance(-1)

    def plot_graph(self) -> None:
        components = self.connected_components()
        min = 0
        max = 10
