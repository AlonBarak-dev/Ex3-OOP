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
<br>
### Visual features <br>
#### Exaples of visual feutures of our graphs that we worked on in the project:
