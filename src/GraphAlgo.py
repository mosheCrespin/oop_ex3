from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
import GraphInterface
from typing import List
from queue import PriorityQueue as PQ
import copy
import collections



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
        list_component=[]
        for i in self.graph.get_all_v().keys():
            if self.shortest_path(id1,i) is not (float('inf'),[]):
                list_component.append(i)
        deep_copied_graph=copy.deepcopy(self.graph)
        temp=deep_copied_graph.get_out_edges()
        deep_copied_graph.set_out_edges(deep_copied_graph.in_edges)
        deep_copied_graph.set_in_edges(temp)
        temporary_list=[]
        for i in deep_copied_graph.get_all_v().keys():
            if self.shortest_path(id1,i) is not (float('inf'),[]):
                temporary_list.append(i)
        return intersection(list_component,temporary_list)

    def connected_components(self) -> List[list]:
        ans=[]
        for i in self.graph.get_all_v():
            temp=sorted(self.connected_component(i))
            if temp not in ans:
                ans.append(temp)
        return ans


    def plot_graph(self) -> None:
        pass

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



