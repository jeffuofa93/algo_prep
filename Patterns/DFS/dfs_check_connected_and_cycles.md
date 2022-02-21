# DFS how to check connected and that their are no cycles

- to check connected in a dfs we just keep a visited set and check if the original size of the graph is equal to the 
  number of visited nodes
- to check for cycles we pass in a previous node to each dfs call and if one of the current nodes neighbors is 
  visted and it is not the previous node then their is a cycle 