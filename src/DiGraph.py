from src.GraphInterface import GraphInterface
import random
import copy


class NodeData:
    random.seed(10)

    def __init__(self, node_id: int, pos: tuple = None, prev: int = -1, distance: float = -1):
        self.id = node_id
        self.pos = pos
        self.prev = prev
        self.distance = distance
        self.degree = 0
        self.parent = self.child = self.left = self.right = None
        if pos is None:
            x = random.uniform(35.0001, 35.0002)
            y = random.uniform(32.0001, 32.0002)
            self.pos = (x, y, 0.0)

    def get_pos(self):
        return self.pos

    def get_node_id(self):
        return self.id

    def __repr__(self):
        return repr((self.id, self.pos))

    def __eq__(self, other):
        if isinstance(other, NodeData):
            return self.id == other.id

    def __lt__(self, other):
        if isinstance(other, NodeData):
            if self.distance < other.distance:
                return 1
            else:
                return 0

    def set_prev(self, prev: int):
        self.prev = prev

    def set_distance(self, distance: float):
        self.distance = distance

    def as_dict(self) -> dict:
        dict = copy.deepcopy(self.__dict__)
        try:
            del dict["prev"]
            del dict["distance"]
            del dict["degree"]
            del dict["parent"]
            del dict["child"]
            del dict["left"]
            del dict["right"]

            x, y, z = self.pos
            converted_pos = f"{x},{y},{z}"
            dict["pos"] = converted_pos
        except Exception as exc:
            print(exc)
        return dict


class DiGraph(GraphInterface):

    def __init__(self):
        self.number_of_nodes = 0
        self.number_of_edges = 0
        self.amount_of_changes = 0
        self.my_graph = {}
        self.out_edges = {}
        self.in_edges = {}

    def __repr__(self):
        str = f"Graph: |V|={self.number_of_nodes} , |E|= {self.number_of_edges}"
        temp = ''
        dict_i = {}
        for i in self.my_graph.keys():
            temp = f"{i}: |edges out| {len(self.all_out_edges_of_node(i))} |edges in| {len(self.all_in_edges_of_node(i))}"
            dict_i[i] = temp
        ll = []
        ll.append(str)
        ll.append(repr(dict_i))
        ans = "\n".join(ll)
        return ans

    def __eq__(self, other):
        if not isinstance(other, DiGraph):
            return False
        if self.number_of_nodes != other.number_of_nodes or self.number_of_edges != other.number_of_edges or self.amount_of_changes != other.amount_of_changes:
            return False
        nodes_set_self = set(self.get_all_v().keys())
        nodes_set_other = set(other.get_all_v().keys())
        final_set = nodes_set_self.intersection(nodes_set_other)
        if len(final_set) != self.number_of_nodes:
            return False
        for i in self.get_all_v().keys():
            if len(set(self.all_out_edges_of_node(i).keys()).intersection(
                    set(other.all_out_edges_of_node(i).keys()))) != len(self.all_out_edges_of_node(i)):
                return False
        return True

    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """

    def v_size(self) -> int:
        return self.number_of_nodes

    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """

    def e_size(self) -> int:
        return self.number_of_edges

    """
    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
    """

    def get_mc(self) -> int:
        return self.amount_of_changes

    def has_edge(self, id1: int, id2: int) -> bool:
        return not self.out_edges.get(id1).get(id2) is None

    def get_node(self, node_id: int) -> NodeData:
        return self.my_graph.get(node_id)

    def get_weight(self, id1: int, id2: int) -> float:
        if not self.has_edge(id1, id2):
            return -1
        else:
            return self.out_edges.get(id1).get(id2)

    """
   Adds an edge to the graph.
   @param id1: The start node of the edge
   @param id2: The end node of the edge
   @param weight: The weight of the edge
   @return: True if the edge was added successfully, False o.w.
   Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
   """

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not self.has_node(id1) or not self.has_node(id2) or weight < 0:
            return False
        if self.has_edge(id1, id2):
            return False
        self.out_edges[id1][id2] = weight
        self.in_edges[id2][id1] = weight
        self.amount_of_changes += 1
        self.number_of_edges += 1

        return True

    """
    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False o.w.
    Note: if the node id already exists the node will not be added
    """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.has_node(node_id):  # the node already exist
            return False
        node = NodeData(node_id, pos)
        self.my_graph[node_id] = node
        self.out_edges[node_id] = {}
        self.in_edges[node_id] = {}
        self.number_of_nodes += 1
        self.amount_of_changes += 1
        return True

    def has_node(self, node_id: int) -> bool:
        return not self.my_graph.get(node_id) is None

    """
    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False o.w.
    Note: if the node id does not exists the function will do nothing
    """

    def remove_node(self, node_id: int) -> bool:
        if not self.has_node(node_id): return False
        counter = 0
        for i in self.in_edges[node_id]:
            del self.out_edges[i][node_id]
            counter += 1
        for i in self.out_edges[node_id]:
            del self.in_edges[i][node_id]
            counter += 1
        del self.my_graph[node_id]
        del self.out_edges[node_id]
        del self.in_edges[node_id]
        self.amount_of_changes += 1
        self.number_of_edges -= counter
        self.number_of_nodes -= 1
        return True

    """
    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False o.w.
    Note: If such an edge does not exists the function will do nothing
    """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if not self.has_node(node_id1) and not self.has_node(node_id2):
            return False
        if not self.has_edge(node_id1, node_id2):
            return False
        del self.out_edges[node_id1][node_id2]
        del self.in_edges[node_id2][node_id1]
        self.number_of_edges -= 1
        self.amount_of_changes += 1
        return True

    """
    return a dictionary of all the nodes in the Graph, each node is represented using a pair
    (node_id, node_data)
    """

    def get_all_v(self) -> dict:
        return self.my_graph

    """
    return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (other_node_id, weight)
    """

    def all_in_edges_of_node(self, id1: int) -> dict:
        if not self.has_node(id1): return {}
        return self.in_edges[id1]

    """
    return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight)
    """

    def all_out_edges_of_node(self, id1: int) -> dict:
        if not self.has_node(id1): return {}
        return self.out_edges[id1]

    def get_out_edges(self) -> dict:
        return self.out_edges

    def get_in_edges(self) -> dict:
        return self.in_edges

    def set_out_edges(self, other: dict) -> None:
        self.out_edges = other

    def set_in_edges(self, other: dict) -> None:
        self.in_edges = other
