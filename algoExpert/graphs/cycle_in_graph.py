""" Cycle in a graph means that we can continously travel between some section of nodes
idea to detect the cycle is we dfs and keep a visited set if we visit a node twice before we visit all nodes then
their is a cycle
"""


def cycle_in_graph(edges):
    num_nodes = len(edges)
    visited = [False for _ in range(num_nodes)]
    cur_stack = [False for _ in range(num_nodes)]

    for node in range(num_nodes):
        if visited[node]:
            continue
        contains_cycle = node_cycle(node, edges, visited, cur_stack)
        if contains_cycle:
            return True
    return False


def node_cycle(node, edges, visited, cur_stack):
    visited[node] = True
    cur_stack[node] = True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            cycle = node_cycle(neighbor, edges, visited, cur_stack)
            if cycle:
                return True
        elif cur_stack[neighbor]:
            return True
    cur_stack[node] = False
    return False


"""
0 -> 1 ,2 
    1 -> 2 
        2 -> None
"""
