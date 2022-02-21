# graph = {
#     0: ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

graph = {
    0: [1, 4],
    1: [0, 2, 4],
    2: [1, 3, 4],
    3: [2, 4],
    4: [0, 1, 2, 3]
}

visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# dfs(visited, graph, 2)

bfsVisited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


graphBFS = {
    0: [1, 4],
    1: [0, 2, 4],
    2: [1, 3, 4],
    3: [2, 4],
    4: [0, 1, 2, 3]
}

def bfs(visitedBFS, graphBFS, node):
    visitedBFS.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graphBFS[s]:
            if neighbour not in visitedBFS:
                visitedBFS.append(neighbour)
                queue.append(neighbour)


# Driver Code
# bfs(bfsVisited, graphBFS, 2)


import itertools

z = list(itertools.permutations([1, 2, 3,4,5]))

for i in z:
    print(i)
