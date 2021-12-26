# Ex3-OOP <br>
<br>

Prof. Boaz Ben Moshe <br>
<br> Submitted by : 
   <br> Alon Barak - 213487598
   <br> Omer Adar - 325022952
   <br>
   ## This repository contains an implementation of directed weighted graphs in Python.<br>
   <br>
   
## Main page

### Projects we thought might be helpful for this assignment: <br>
   - [ Directed graph explination ](https://en.wikipedia.org/wiki/Directed_graph) <br>
   - [ Travelling salesman problem ](https://en.wikipedia.org/wiki/Travelling_salesman_problem) <br>
   - [ How to check if a directed graph is connected or not](https://www.geeksforgeeks.org/check-if-a-directed-graph-is-connected-or-not/) <br>
   - [ Dijkstra's algorithm ](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) <br>
   - [ Depth-first search ](https://en.wikipedia.org/wiki/Depth-first_search) <br>

## Featurs <br>
### Graph features <br>
In this repository contains graph algorithms which are helpful for a wide range of options such as:
- Save / Load a graph:
```ruby 
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
file = "../data/T0.json"
g_algo.load_from_json(file)  # init a GraphAlgo from a json file
print(g_algo.shortest_path(0, 3))
print(g_algo.shortest_path(3, 1))
print(g_algo.centerPoint())
g_algo.save_to_json(file + '_saved')
```
- Find the shortest path between nodes using Dijkstra and get their distance:
```ruby 
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
g = DiGraph()  # creates an empty directed graph
for n in range(4):
   g.add_node(n)
g.add_edge(0, 1, 1)
g.add_edge(1, 0, 1.1)
g.add_edge(1, 2, 1.3)
g.add_edge(2, 3, 1.1)
g.add_edge(1, 3, 1.9)
g.remove_edge(1, 3)
g.add_edge(1, 3, 10)
print(g)  # prints the __repr__ (func output)
print(g.get_all_v())  # prints a dict with all the graph's vertices.
print(g.all_in_edges_of_node(1))
print(g.all_out_edges_of_node(1))
g_algo = GraphAlgo(g)
print(g_algo.shortest_path(0, 3))
```
- Find the cented node of the graph(centerPoint()) and the shortest path that visits all the nodes in the list (TSP):
```ruby
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
g = DiGraph()  # creates an empty directed graph
for n in range(5):
   g.add_node(n)
g.add_edge(0, 1, 1)
g.add_edge(0, 4, 5)
g.add_edge(1, 0, 1.1)
g.add_edge(1, 2, 1.3)
g.add_edge(1, 3, 1.9)
g.add_edge(2, 3, 1.1)
g.add_edge(3, 4, 2.1)
g.add_edge(4, 2, .5)
g_algo = GraphAlgo(g)
print(g_algo.centerPoint())
print(g_algo.TSP([1, 2, 4]))    
```

### Visual features <br>
#### Exaples of visual feutures of our graphs that we worked on in the project:
![A5json](https://user-images.githubusercontent.com/80644255/147408577-9962c8c0-86b3-47d2-9868-a1eb8f140b39.png)
- #### A graph before a removal of nodes:
![A2json-before_remove (1)](https://user-images.githubusercontent.com/80644255/147409248-ef204c0f-f71e-4e8e-93b2-18b7d9933a5f.png)
- #### The same graph after the removal:
![A2json-after_remove](https://user-images.githubusercontent.com/80644255/147409269-4eef5439-4de8-4f9d-b4e3-1d3054ee6657.png)
- #### A plot in a random but elegant manner for nodes without given positions in the graph:
![T0json](https://user-images.githubusercontent.com/80644255/147409439-d1158142-8a84-4a72-b23e-8fc7135a2e79.png)

## UML diagram of the project:
![image](https://user-images.githubusercontent.com/80644255/147421378-f371cca6-4fb6-4f43-a639-2228a8161db3.png)

