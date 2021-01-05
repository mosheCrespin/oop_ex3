from src.GraphInterface import GraphInterface


class NodeData:
    def __init__(self, node_id: int, pos: tuple = None, prev: int = -1, distance: float = -1):
        self.node_id = node_id
        self.pos = pos
        self.prev = prev
        self.distance = distance

    def __repr__(self):
        return repr((self.node_id, self.pos))

    def __eq__(self, other):
        if isinstance(other, NodeData):
            return self.node_id == other.node_id

    def __cmp__(self, other):
        if isinstance(other, NodeData):
            if (self.distance > other.distance):
                return 1
            if (self.distance < other.distance):
                return -1
            return 0

    def id(self):
        return self.node_id

    def set_prev(self, prev: int):
        self.prev = prev

    def set_distance(self, distance: float):
        self.distance = distance


class DiGraph(GraphInterface):

    def __init__(self):
        self.number_of_nodes = 0
        self.number_of_edges = 0
        self.amount_of_changes = 0
        self.my_graph = {}
        self.out_edges = {}
        self.in_edges = {}

    def v_size(self) -> int:
        return self.number_of_nodes

    def e_size(self) -> int:
        return self.number_of_edges

    def get_mc(self) -> int:
        return self.amount_of_changes

    def has_edge(self, id1: int, id2: int) -> bool:
        return not self.out_edges.get(id1).get(id2) is None


    def get_node (self, node_id: int) -> NodeData:
        return self.my_graph.get(node_id)


    def get_weight(self, id1: int, id2: int) -> float:
        if not self.has_edge(id1, id2):
            return -1
        else:
            return self.out_edges.get(id1).get(id2)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if not self.has_node(id1) or not self.has_node(id2):
            return False
        if self.has_edge(id1, id2):
            return False
        self.out_edges[id1][id2] = weight
        self.in_edges[id2][id1] = weight
        self.amount_of_changes += 1
        self.number_of_edges += 1
        return True

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

    def get_all_v(self) -> dict:
        return self.my_graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        if not self.has_node(id1): return None
        return self.in_edges[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        if not self.has_node(id1): return None
        return self.out_edges[id1]
