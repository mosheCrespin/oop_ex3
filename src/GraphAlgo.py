from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import GraphInterface
from queue import PriorityQueue as PQ
import copy

class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = None):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        graph_ans = copy.copy(self.graph)
        return graph_ans


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = 'inf'
        path_list = []

        if not self.graph.has_node(id1) or not self.graph.has_node(id2) or self.graph.all_in_edges_of_node(id2) is None:
            return (path, path_list)

        if id1 == id2:
            path = 0
            path_list.append(self)
            return (path, path_list)

        self.reset_prevAndDist()
        self.dijkstra(id2, id2)

        path = self.graph.get_node(id2).distance
        path_list.insert(0,id2)
        node_prev = self.graph.get_node(id2).prev

        if(path != -1):
            while(node_prev != id1):
                path_list.insert(0, node_prev)
                node_prev =self.graph.get_node(node_prev).prev
            path_list.insert(0, id1)
        else:
            path = 'inf'

        return (path, path_list)

    def dijkstra (self, start: int, dest: int):
        priority_qeueu = PQ()
        node_curr = self.graph.get_node(start)
        node_curr.set_prev(start)
        priority_qeueu.put(node_curr)

        while (priority_qeueu.not_empty and node_curr.id() != dest):

            node_curr = priority_qeueu.get()

            for key in self.graph.all_out_edges_of_node(node_curr.id()).keys():
                node_na = self.graph.get_node(key)
                edge_weight = self.graph.get_weight(node_curr.id(), key)

                if (node_na.prev == -1):
                    node_na.set_prev(node_curr.id())
                    node_na.set_distance(node_curr.distance+edge_weight)
                    priority_qeueu.put(node_na)

                elif (node_na.distance > node_curr.distance + edge_weight):
                    node_na.set_prev(node_curr.id())
                    node_na.set_distance(node_curr.distance + edge_weight)



    def reset_prevAndDist (self):
        for node in self.graph.my_graph.values():
            node.set_prev(-1)
            node.set_distance(-1)
