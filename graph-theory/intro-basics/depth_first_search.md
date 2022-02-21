# Depth First Search 

- DFS fundamental graph search algorithm with complexity of O(V+E)
- By itself it's not that useful can be augmented to perform other tasks such as count connected components, determine connectivity or find bridges/articulation points 

## Basic DFS

- We pick a start node, mark the start node as visited and recursively visit nodes that have not been visited yet
```python
# n = number of nodes in the graph 
# g = adjaceny list representing graph
visited = [False * n]

function dfs(node):
  if visited[node]:
    visited[node] = True
  neighbors = g[node]
  for next in neighbors:
    dfs(next)

# start dfs at node 0 
start_node = 0
dfs(start_node)
```

## Connected components

- Identify components by coloring nodes 
- We can use DFS to Identify components 
```python
# Global variables
n = number of nodes in the graph
g = adj list 
count = 0
components = [0 * n]
visted = [False * n]

function findComponents():
  for i in range(len(n)):
    if !visited[i]:
      count += 1 
      dfs(i)
  return (count,components)

function dfs(node):
  visited[node] = True
  components[node] = count
  for next in g[node]:
    if !visited[next]:
      dfs(next)
```

## What Else can  DFS do

- Compute MST 
- Detect and find cycles in graph
- Check if graph is bipartite
- Find strongly connected components
- Topologically sort the nodes of a graph
- Find bridges and articulations points
- Find augmenting paths in a flow network
- Generate mazes
