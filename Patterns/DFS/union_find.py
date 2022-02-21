def union_find(n, edges):
    nums = [-1 for x in range(n)]

    def find(idx):
        if nums[idx] == -1:
            return idx
        return find(nums[idx])

    for i in range(len(edges)):

        x = find(edges[i][0])
        y = find(edges[i][1])
        print(f"x={edges[i][0]} y={edges[i][1]}")
        if x == y:
            return False
        # union
        nums[x] = y
        print(nums)
    return len(edges) == n - 1


"""
x = 0
y = 1

0's parent becomes 1 
[1,-1,-1,-1,-1]

x = 0, y = 2 
1's parent becomes 2




"""


def validTree(n, edges):
    parent = [x for x in range(n)]

    def find(x):
        return x if parent[x] == x else find(parent[x])

    for e in edges:
        x = find(e[0])
        y = find(e[1])
        if x == y:
            return False
        parent[x] = y
        print(parent)
        print()
    return len(edges) == n - 1


n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(validTree(n, edges))
