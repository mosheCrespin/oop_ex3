from src import DiGraph
from src.DiGraph import NodeData

"""
This class implements Fibonacci Heap 
the implementation based on https://github.com/danielborowski/fibonacci-heap-python 
insert - O(1)
extract_min - O(log n)
"""

class fiboHeap:

        def __init__(self):
            self.root_list = None
            self.min_node = None
            self.size = 0

        # function to iterate through a doubly linked list
        def iterate(self, head):
            node = stop = head
            flag = False
            while True:
                if node == stop and flag is True:
                    break
                elif node == stop:
                    flag = True
                yield node
                node = node.right

        """
         extract (delete) the min node from the heap in O(log n) time
        """
        def extract_min(self):
            z = self.min_node
            if z is not None:
                if z.child is not None:
                    # attach child nodes to root list
                    children = [x for x in self.iterate(z.child)]
                    for i in range(0, len(children)):
                        self.merge_with_root_list(children[i])
                        children[i].parent = None
                self.remove_from_root_list(z)
                # set new min node in heap
                if z == z.right:
                    self.min_node = self.root_list = None
                else:
                    self.min_node = z.right
                    self.consolidate()
                self.size -= 1
            return z

        """
        insert new node into the unordered root list in O(1) time
        """
        def insert(self, n: NodeData):
            n.left = n.right = n
            self.merge_with_root_list(n)
            if self.min_node is None or n.distance < self.min_node.distance:
                self.min_node = n
            self.size += 1
            return n

        """
         combine root nodes of equal degree to consolidate the heap
         by creating a list of unordered binomial trees
        """
        def consolidate(self):
            A = [None] * self.size
            nodes = [w for w in self.iterate(self.root_list)]
            for w in range(0, len(nodes)):
                x = nodes[w]
                d = x.degree
                while A[d] != None:
                    y = A[d]
                    if x.distance > y.distance:
                        temp = x
                        x, y = y, temp
                    self.heap_link(y, x)
                    A[d] = None
                    d += 1
                A[d] = x
            # find new min node - no need to reconstruct new root list below
            # because root list was iteratively changing as we were moving
            # nodes around in the above loop
            for i in range(0, len(A)):
                if A[i] is not None:
                    if A[i].distance < self.min_node.distance:
                        self.min_node = A[i]

        """
        actual linking of one node to another in the root list
        updates the child linked list
        """
        def heap_link(self, y, x):
            self.remove_from_root_list(y)
            y.left = y.right = y
            self.merge_with_child_list(x, y)
            x.degree += 1
            y.parent = x
            y.mark = False

        """
         merge a node with the doubly linked root list
        """
        def merge_with_root_list(self, node):
            if self.root_list is None:
                self.root_list = node
            else:
                node.right = self.root_list.right
                node.left = self.root_list
                self.root_list.right.left = node
                self.root_list.right = node

        """
         merge a node with the doubly linked child list of a root node
        """
        def merge_with_child_list(self, parent, node):
            if parent.child is None:
                parent.child = node
            else:
                node.right = parent.child.right
                node.left = parent.child
                parent.child.right.left = node
                parent.child.right = node

        """
        remove a node from the doubly linked root list
        """
        def remove_from_root_list(self, node):
            if node == self.root_list:
                self.root_list = node.right
            node.left.right = node.right
            node.right.left = node.left

        """
        remove a node from the doubly linked child list
        """
        def remove_from_child_list(self, parent, node):
            if parent.child == parent.child.right:
                parent.child = None
            elif parent.child == node:
                parent.child = node.right
                node.right.parent = parent
            node.left.right = node.right
            node.right.left = node.left