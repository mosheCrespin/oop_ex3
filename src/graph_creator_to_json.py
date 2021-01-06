from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import random


class graph_creator:

    def __init__(self):
        self.graph=DiGraph()

    def creator(self, node_size: int, edge_size: int, seed : int,number_of_connected_componnets:int):
        random.seed(seed)
        edges_counter=int(edge_size/node_size)
        counter=edges_counter
        jump=int(node_size/number_of_connected_componnets)
        for i in range(0, node_size):
            self.graph.add_node(i)
        for i in range(0,node_size,jump):
            for j in range(i,i+jump):
                while counter>1 :
                    if self.graph.add_edge(j, random.randint(i, i+jump), random.uniform(0, 3)):
                        counter-=1
                while not self.graph.add_edge(j, random.randint(0,node_size), random.uniform(0, 3)):
                    counter = edges_counter

    def save_to_json(self,file_name:str):
        ga=GraphAlgo(self.graph)
        ga.save_to_json(file_name)



if __name__ == '__main__':
    graph=graph_creator()
    graph.creator(pow(10,3),pow(10,4),3,120)
    file="created_graph.json"
    graph.save_to_json(file)













