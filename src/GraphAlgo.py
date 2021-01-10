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
from src.fibonacciHeap import fiboHeap
from queue import PriorityQueue as PQ


def intersection(l1, l2):
    return [value for value in l1 if value in l2]


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        if g is None:
            g = DiGraph()
        self.graph = g

    """
    This method return the graph on which the algorithm works on.
    Complexity: O(1)
    """
    def get_graph(self) -> GraphInterface:
        return self.graph

    """
    This method loads graph from json file.
    @param file_name: The path to the json file
    @returns True if the loading was successful, else returns False 
    """
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

    """
    This method returns the graph in json format
    """

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

    """
    This method Saves the graph in JSON format to  file
    @param file_name: The path to the out file
    @return: True if the save was successful, else returns False 
    """

    def save_to_json(self, file_name: str) -> bool:
        graph_to_dict = self.serialize()
        try:
            with open(file_name, "w") as file:

                json.dump(graph_to_dict, default=lambda l: l.as_dict(), indent=4,
                          fp=file)  # for all objects in graph dump as dict


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

    """
    Finds the Strongly Connected Component(SCC) that node id1 is a part of.
    @param id1: The node id
    @return: The list of nodes in the SCC
    """

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

    """
    Finds all the Strongly Connected Component(SCC) in the graph.
    @return: The list all SCC
    """

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

    """
    This method get 2 nodes and calculate the shortest path between them.
    If there is a path than the method returns the sum of the weights and list of shortest path  (distance,[path list])
    If there is no path or if one of the nodes does not exist in the graph, than returns returns (float('inf'),[])
    If id1==id2 than returns (0,[])
    Shortest path implementation relies on Dijkstra Algorithm 
    Complexity: O((|E|+|V|) log|V|)
    @param id1: The start node id
    @param id2: The end node id
    @return: The distance of the path, a list of the nodes ids that the path goes through
    """

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = float('inf')
        path_list = []

        if not self.graph.has_node(id1) or not self.graph.has_node(id2):  # if one of nodes not in graph
            return (path, path_list)

        if id1 == id2:  # path from node to itself
            path = 0
            path_list.append(id1)
            return (path, path_list)

        self.reset_prevAndDist()  # reset all predecessors and dist to -1
        self.dijkstra(id1, id2)  # update predecessors and dist using dijkstra

        path = self.graph.get_node(id2).distance
        if path != -1:  # if there is path
            path_list.insert(0, id2)
            node_prev = self.graph.get_node(id2).prev
            while node_prev != id1:  # go through all predecessors and add to list
                path_list.insert(0, node_prev)
                node_prev = self.graph.get_node(node_prev).prev
            path_list.insert(0, id1)

        else:  # if there is no path
            path = float('inf')

        return (path, path_list)

    """
    This method travers the graph through nodes neighbors using dijkstra's algorithm using Priority Queue
    The priority-qeueu prior the nodes by smallest sum of weights from node start.
    This method sets all nodes predecessor and shortest dist in the path from start to dest.
    Complexity: O((|E|+|V|) log|V|)
    @param start: The start node id
    @param dest: The end node id
    """

    def dijkstra(self, start: int, dest: int):

        priority_qeueu = PQ()
        node_curr = self.graph.get_node(start) # the node to explore
        node_curr.set_prev(start) # set start predecessor to itself
        node_curr.set_distance(0) # set start dist to 0
        priority_qeueu.put(node_curr) # add start to priority qeueue

        while priority_qeueu.qsize() != 0 and node_curr.get_node_id() != dest: # while priority qeueue not empty and node dest not explored yet
            node_curr = priority_qeueu.get() # explore the next node in priority qeueu
            for key in self.graph.all_out_edges_of_node(node_curr.get_node_id()).keys(): # go through all node curr neighbours
                node_na = self.graph.get_node(key) # neighbour to check
                edge_weight = self.graph.get_weight(node_curr.get_node_id(), key) # the edge weight between node_curr to node_na

                if node_na.prev == -1: # if node_na not visited
                    node_na.set_prev(node_curr.get_node_id()) # set node_na predecessor to node_curr
                    node_na.set_distance(node_curr.distance + edge_weight) # set dist to sum of weights
                    priority_qeueu.put(node_na)

                elif node_na.distance > node_curr.distance + edge_weight: # if node_na visited compare the dist from start, if the new path is better: update predecessor and dist
                    node_na.set_prev(node_curr.get_node_id()) # update predecessor
                    node_na.set_distance(node_curr.distance + edge_weight) # update dist from start


    """
    This method run over all the nodes and update there prev and dist to -1.
    Complexity: 0(n)
    """
    def reset_prevAndDist(self):
        for node in self.graph.my_graph.values():
            node.set_prev(-1)
            node.set_distance(-1)

    def drawArrow(self, p1, p2, head_width, width):
        plt.arrow(p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1],
                  visible=True, ec="blue", width=width / 100, head_width=head_width / 2, fc="blue", in_layout=True,
                  length_includes_head=True)

    """
    Plots the graph.
    If the nodes have a position, the nodes will be placed there.
    Otherwise, they will be placed in a random but elegant manner.
    @return: None
    """

    def plot_graph(self) -> None:
        fig, ax = plt.subplots()
        x_smaller_range = 200
        y_smaller_range = 200
        old_x = 0
        old_y = 0

        ll = self.get_graph().get_all_v().keys()
        for i in ll:
            node = self.get_graph().get_node(i)
            x, y, z = node.get_pos()
            plt.plot(x, y, 'o', color='blue',
                     markersize=15, linewidth=10,
                     markerfacecolor='white',
                     markeredgecolor='black',
                     markeredgewidth=1)

            if abs(old_x - x) < x_smaller_range:
                x_smaller_range = abs(old_x - x)
                old_x = x
            if abs(old_y - y) < y_smaller_range:
                y_smaller_range = abs(old_y - y)
                old_y = y
            # ax.annotate(i.get_node_id(), (x - 0.009, y - 0.009),
            #             color='blue',
            #             fontsize=8)  # draw id
        print(f"y range:{y_smaller_range}, x range:{x_smaller_range}")

        for i in ll:
            node = self.get_graph().get_node(i)
            x, y, z = node.get_pos()
            ax.annotate(node.get_node_id(), (x, y + y_smaller_range),
                        color='black',
                        fontsize=10)  # draw id

        for i in ll:
            node = self.get_graph().get_node(i)
            x, y, z = node.get_pos()
            curr_point = np.array([x, y])
            for j in self.get_graph().all_out_edges_of_node(i).keys():
                adj = self.get_graph().get_node(j)
                x_adj, y_adj, z_adj = adj.get_pos()
                adj_point = np.array([x_adj, y_adj])
                self.drawArrow(curr_point, adj_point, x_smaller_range, y_smaller_range)

        plt.show()

    # def plot_graph(self) -> None:
    # a=[value for value in self.get_graph().get_all_v().values()]
    # x_vals=[]
    # y_vals=[]
    # ids=[]
    # print(a)
    # for node in a:
    #     ids.append(node.get_node_id())
    #     x,y,z=node.get_pos()
    #     x_vals.append(x)
    #     y_vals.append(y)
    #     # position.append(pos.get_pos())
    # ax.scatter(x_vals, y_vals)

    # sorted_pos_x=sorted(position, key=itemgetter(0), reverse=True)

    # x_smaller_range = 200
    # y_smaller_range=200
    #
    # old_x=0
    # old_y=0
    # for i in self.get_graph().get_all_v().values():
    #     x, y, z = i.get_pos()
    #     if abs(old_x-x) < x_smaller_range:
    #         x_smaller_range=abs(old_x-x)
    #         old_x=x
    #     if abs(old_y-y) < y_smaller_range:
    #         y_smaller_range=abs(old_y-y)
    #         old_y=y

    # for i in self.get_graph().get_all_v().values():
    #     x, y, z = i.get_pos()
    #     plt.plot(x, y, 'o', color='blue',
    #              markersize=15, linewidth=10,
    #              markerfacecolor='white',
    #              markeredgecolor='black',
    #              markeredgewidth=1)
    #     ax.annotate(i.get_node_id(), (x-x_smaller_range, y),
    #                 color='black',
    #                 fontsize=10)  # draw id
    #     curr_point = np.array([x, y])
    #     for j in self.get_graph().all_out_edges_of_node(i.get_node_id()).keys():
    #         adj = self.get_graph().get_node(j)
    #         x_adj, y_adj, z_adj = adj.get_pos()
    #         adj_point = np.array([x_adj, y_adj])
    #         self.drawArrow(curr_point, adj_point,x_smaller_range,y_smaller_range)
    #
    # plt.show()

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

    # def dijkstra(self, start: int, dest: int):
    #
    #     fib_heap = fiboHeap()
    #     node_curr = self.graph.get_node(start)
    #     node_curr.set_prev(start)
    #     node_curr.set_distance(0)
    #     fib_heap.insert(node_curr)
    #
    #     while fib_heap.size != 0 and node_curr.get_node_id() != dest:
    #         node_curr = fib_heap.extract_min()
    #         for key in self.graph.all_out_edges_of_node(node_curr.get_node_id()).keys():
    #             node_na = self.graph.get_node(key)
    #             edge_weight = self.graph.get_weight(node_curr.get_node_id(), key)
    #
    #             if node_na.prev == -1:
    #                 node_na.set_prev(node_curr.get_node_id())
    #                 node_na.set_distance(node_curr.distance + edge_weight)
    #                 fib_heap.insert(node_na)
    #
    #             elif node_na.distance > node_curr.distance + edge_weight:
    #                 node_na.set_prev(node_curr.get_node_id())
    #                 node_na.set_distance(node_curr.distance + edge_weight)
