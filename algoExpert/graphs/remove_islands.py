"""
okay similiar to before we have a flood fill problem
this issue I'm having with this one is that we either need to check and clear out all the touching islands before or
need to do it on the fly

first lets find the touching sections
I think we should just dfs and mark
"""


def removeIslands(matrix):
    # Write your code here
    height = len(matrix)
    width = len(matrix[0])
    copy = [[0 for _ in row] for row in matrix]
    for i in range(height):
        for j in range(width):
            if i == height - 1 or i == 0 or j == 0 or j == width - 1:
                dfs(i, j, matrix, copy)
    return copy


def dfs(i, j, matrix, copy):
    if i >= len(matrix) or i < 0 or j >= len(matrix[i]) or j < 0:
        return
    if matrix[i][j] == 0:
        return
    copy[i][j] = 1
    matrix[i][j] = 0
    dfs(i + 1, j, matrix, copy)
    dfs(i - 1, j, matrix, copy)
    dfs(i, j - 1, matrix, copy)
    dfs(i, j + 1, matrix, copy)
