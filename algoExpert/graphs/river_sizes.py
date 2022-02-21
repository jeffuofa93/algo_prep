"""
Big idea dfs in any direction from any ones that you find

For each visited node add it's tuple to a set to check if the node is visited
"""


def riverSizes(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                result.append(dfs(i, j, matrix))
    return result


def dfs(i, j, matrix):
    matrix[i][j] = 0
    size = 1
    possible_moves = [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
    for move_i, move_j in possible_moves:
        if not invalid_coord(move_i, move_j, matrix):
            size += dfs(move_i, move_j, matrix)
    return size


def invalid_coord(i, j, matrix):
    return (
        i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) or matrix[i][j] == 0
    )


x = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

print(riverSizes(x))
