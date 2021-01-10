# ex3

### **About:**
*this project is used for an implementation of a directed (positive) Weighted Graph in python language.*
*in addition we compared the run-time complexity of this project, with a similar project written in Java (ex2) and with networkX library. you can see more about that in our  [Wiki](https://github.com/mosheCrespin/oop_ex3/wiki)*.


![](https://github.com/mosheCrespin/oop_ex3/blob/master/src/tests/Compare_img/readmeGraph.PNG)

### **how to start?**
first clone this repository using this following command:
 ```
$git clone https://github.com/mosheCrespin/oop_ex3.git
 ```
once the clone finishd there will be an `oop_ex3` folder inside you will see the project.

### **some info:**
*there are 3 classes inside `src`-> `NodeData` ,`DiGraph`, `GraphAlgo`;
*also there is a package called `tests` inside there are all the tests of this project and also inside this repository there is a directory called `comapring_files` that contains all the comparing files for this project, see more about that in our `Wiki` page.

### **classes**
-------------------------
**NodeData**

*this class represents a single vertex of the graph. Each node has 2 instance variables: `key`-a unique  id for this node. `pos`- the position of this vertex, if in the init part of the vertex, the constructor did'nt get the position, then the position will be a random position.there are 4 more instance variables that used for the algorithm part of this prioject- `prev` `distance` `degree` `parent`. 
*In this class there are getters and setters and there is `__repr__` method;

*the `as_dict` nethod return a dictionary copy of this vertex (used for saving the graph to json format)


----------------------------------

**DiGraph**

*this class represents a directed (positive) Weighted Graph. this class using NodeData class for the vertex of the graph. each object of this class contains a data structure who holds the nodes of the graph(in dictionary `id` as key `NodeData` as value) called `my_graph`. in addition there are two more dictionaries represents the edges of the graph- `out_edges` represents all the edges of this graph, `in_edges` represents the graph transpose
in addition, there are 3 instance variables: `number_of_nodes`- the amount of nodes in the graph, `number_of_edges`- the amount of edges in the graph, `amount_of_changes`- the amount of changes made on the graph;

*In this class there are getters for the Instance variables and `__repr__()` ans `__eq__` methods;

* `get_all_v()`-  returns all the vertex of this graph as dictionary format; **_`O(1)`_**

* `all_in_edges_of_node(key)`- returns all the nodes connected to (into) the given node; **_`O(1)`_**

* `all_out_edges_of_node(key)`- returns all the nodes connected from the given node; **_`O(1)`_**


* `add_edge(key1,key2,weight)`- - connect between the given nodes with the given weight. if there is alredy an edge between the nodes or one of the nodes does not exist in the graph, or the weight is negative then the method returns false o.w return true; **_`O(1)`_**

* `addNode(key, pos:None)`- adds the node with the given id and pos to the graph, if the node already exist in the graph, the function does not add this node again, if the pos is none then the positiion will be a random position; **_`O(1)`_**

* `hasEdge(key1,key2)`- method, check if the given nodes has edge who connect them; **_`O(1)`_**


* `get_weight(node1,node2)`- method uses `hasEdge()` method to check if there is an edge between the given nodes, if not the method returns -1. if yes then the method returns the weight between the given nodes; **_`O(1)`_**

* `remove_node(key)`- removes the node from the graph and all of his edges, returns true if the node removed successfully, false o.w; 
**_`O(K), K = degree of node_id`_**

* `remove_edge(key1,key2)`- method uses `hasEdge()` method to check if there is an edge between the given nodes. if yes then the method removes the edge between the given nodes. else the method return false; **_`O(1)`_**

* `get_node(key)`-  returns the node with the given id if this node exist in this graph; **_`O(1)`_**

------------------------

**GraphAlgo**

*this class represents the Theory algorithms for an a directed weighted(positive) graph;

*the `get_graph()` method simply returns the graph;

*the `load_from_json(file_name)` method simply load the the graph from the given json file, if there is no such file in the memory then the graph will remain with no differences. the method returns `true` or `false` depends on if the process succeeded;

*the `save_to_json(file_name)` method simply save the graph to a json format, the method returns `true` or `false` depends on if the process succeeded;

*the `connected_component(id)` method returns a list of the Strongly Connected Component(SCC) that the given node is a part of. this method using `dfs` algorithm 2 times, the first time is on the regular graph, the second time is on the transpose of this graph.  

*the `connected_components()` method returns a list of lists, represents all the SCC of this graph this method using `connected_component()` method;

*the `shortestPath(src, dest)` method, this method using in Dijkstra's algorithm. it returns a Tuple with the distance of the path and the actual path between `src` to `dest` via List of keys. if `src` or `dest` are not in the graph or one of them does not exist in the graph, than the method returns `(float('inf',[])`. if `src` is equal to `dest` then the method returns a list with only `src`.

*the `plot_graph()` method simply plot this graph, the nodes will be in there given position.



> #### `Dijkstra's algorithm`:
>
>![](https://github.com/mosheCrespin/oop_ex3/blob/master/src/tests/Compare_img/Dijkstra.PNG)
>
> Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph
>
> the implementation relies on using Priority Queue
>
> the time complexity is O((|E|+|V|)log |V|)
>
> for more reading- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm



















