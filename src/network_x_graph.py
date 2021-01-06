import json

import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.components.strongly_connected as nx_strong



class network_x:

    def __init__(self):
        self.graph = nx.DiGraph()

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                loaded_graph = nx.DiGraph()
                f = json.load(file)
                for node in f.get("Nodes"):
                    id = node.get("id")
                    pos = None
                    if node.get("pos") is not None:
                        list_pos = node.get("pos").split(",")
                        x = float(list_pos[0])
                        y = float(list_pos[1])
                        pos = (x, y)
                    loaded_graph.add_node(id, pos=pos)
                for edge in f.get("Edges"):
                    src = edge.get("src")
                    dest = edge.get("dest")
                    w = edge.get("w")
                    loaded_graph.add_edge(src, dest, weight=w)
                self.graph = loaded_graph

        except IOError as exp:
            print(exp)
            return False
        return True


    def shortest_path(self,src:int,dest:int):
        # print(nx.get_node_attributes(self.graph, 'weight'))
        print(nx.shortest_path_length(self.graph,src,dest,weight='weight'))
        return nx.shortest_path(self.graph,src,dest,weight='weight')

    def draw_graph(self):
        nx.draw_networkx(self.graph, nx.get_node_attributes(self.graph, 'pos'), arrows=True, with_labels=True)
        plt.show()


    def connected_componnets(self):
        # b=nx_strong.condensation(self.graph)
        print(nx_strong.number_strongly_connected_components(self.graph))


    def save_to_json(self):
        with open('networkdata1.json', 'w') as outfile1:
            outfile1.write(json.dumps(nx.node_link_data(self.graph)))






