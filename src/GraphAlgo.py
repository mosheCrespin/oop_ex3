from abc import ABC

from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from typing import List
import json
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from matplotlib.patches import ConnectionPatch

class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = None):
        if g is None:
            g = DiGraph()
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                loaded_graph = DiGraph()
                f = json.load(file)
                for node in f.get("Nodes"):
                    id = node.get("id")
                    pos = None
                    if node.get("pos") is not None:
                        list_pos = node.get("pos").split(",")
                        x = float(list_pos[0])
                        y = float(list_pos[1])
                        z = float(list_pos[2])
                        pos = (x, y, z)
                    loaded_graph.add_node(id, pos)
                for edge in f.get("Edges"):
                    src = edge.get("src")
                    dest = edge.get("dest")
                    w = edge.get("w")
                    loaded_graph.add_edge(src, dest, w)
                self.graph = loaded_graph

        except IOError as exp:
            print(exp)
            return False
        return True

    def serialize(self):
        to_dict = {}
        edge_to_dict = []
        to_dict["Nodes"] = [node for node in self.graph.my_graph.values()]
        for src in self.graph.my_graph:
            for dest, weight in self.get_graph().all_out_edges_of_node(src).items():
                temp = {"src": src, "dest": dest, "w": weight}
                edge_to_dict.append(temp)

        to_dict["Edges"] = edge_to_dict
        return to_dict

    def save_to_json(self, file_name: str) -> bool:
        graph_to_dict = self.serialize()
        try:
            with open(file_name, "w") as file:
                json.dump(graph_to_dict, default=lambda l: l.as_dict(), indent=4, fp=file)

        except IOError as exp:
            print(exp)
            return False
        return True

    def dfs_algorithm_find_connected_nodes(self, id: int, old_dict: dict = None) -> list:
        stack = deque()
        visited = {}
        ans = [id]
        stack.append(id)  # add the first node to the stack
        visited[id] = 1
        while len(stack) != 0:
            curr = stack.pop()
            for adj in self.get_graph().all_out_edges_of_node(curr).keys():
                if visited.get(adj) != 1:
                    stack.append(adj)
                    visited[adj] = 1
                    if old_dict is None:
                        ans.append(adj)
                    elif old_dict.get(adj) == 1:
                        ans.append(adj)
        return ans

    def connected_component(self, id1: int) -> list:
        if not self.get_graph().has_node(id1):
            return []
        dict_intersection = {}
        list_component_a = self.dfs_algorithm_find_connected_nodes(id1)
        remember_out = self.get_graph().get_out_edges()
        remember_in = self.get_graph().get_in_edges()
        self.get_graph().set_out_edges(remember_in)
        self.get_graph().set_in_edges(remember_out)
        for i in list_component_a:
            dict_intersection[i] = 1
        list_component_b = self.dfs_algorithm_find_connected_nodes(id1, dict_intersection)
        self.get_graph().set_out_edges(remember_out)
        self.get_graph().set_in_edges(remember_in)
        return list_component_b

    def connected_components(self) -> List[list]:
        ans = []
        visited = {}
        for i in self.graph.get_all_v():
            if visited.get(i) != 1:
                ll = self.connected_component(i)
                for j in ll:
                    visited[j] = 1
                ans.append(ll)
        return ans



    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        fig, ax = plt.subplots()
        all_v = self.graph.get_all_v().keys()
        for node in all_v:
            x, y, z = self.graph.get_node(node).get_pos()
            curr_point = np.array([x, y])
            xyA = curr_point
            ax.annotate(self.graph.get_node(node).get_node_id(), (x, y),
                        color='black',
                        fontsize=12)  # draw id
            for e in self.graph.all_out_edges_of_node(node).keys():
                x, y, z = self.graph.get_node(e).get_pos()
                curr_point = np.array([x, y])
                xyB = curr_point
                con = ConnectionPatch(xyA, xyB, "data", "data",
                                      arrowstyle="-|>", shrinkA=6, shrinkB=6,
                                      mutation_scale=14, fc="black", color="black")
                ax.plot([xyA[0], xyB[0]], [xyA[1], xyB[1]], "o", color='gray', markersize=8, linewidth=10)
                ax.add_artist(con)

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("My Python Graph")
        plt.show()

