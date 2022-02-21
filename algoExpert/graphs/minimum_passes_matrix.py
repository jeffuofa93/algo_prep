"""
we are changing any negative values to positive only if their is at least 1 positive value connected to the negative
value in 4 directions

we are returning the minimum number of passes to convert the entire array to positives

naive approach iterate over the array as many times as it takes to get rid of all the negatives if we can't get rid
of all negatives return -1

Okay so how can we optimizes
so if we are at a value we can change, we should check if their
"""
from collections import deque


def minimumPassesOfMatrix(matrix):
    # Write your code here.
    # first lets get the position of all the negative values in the map
    # find all positive values and add it to q1
    # take the q
    q1 = deque()
    q2 = deque()
    neg_set = deque()
    count = 0
    for i in range(len(matrix)):
        for j, val in enumerate(matrix[i]):
            if val > 0:
                q1.append((i, j))
            if val < 0:
                neg_set.append((i, j))
    q1_turn = True
    while True:
        cur_q = q1 if q1_turn else q2
        next_q = q2 if q1_turn else q1
        while cur_q:
            i, j = cur_q.popleft()
            find_more_nodes(i + 1, j, matrix, next_q, neg_set)
            find_more_nodes(i - 1, j, matrix, next_q, neg_set)
            find_more_nodes(i, j - 1, matrix, next_q, neg_set)
            find_more_nodes(i, j + 1, matrix, next_q, neg_set)
        count += 1
        if not q1 and not q2:
            return count - 1 if len(neg_set) == 0 else -1
        q1_turn = not q1_turn


def find_more_nodes(i, j, matrix, next_q, neq_set):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]):
        return
    cur_node = matrix[i][j]
    if cur_node < 0:
        neq_set.remove((i, j))
        next_q.append((i, j))
        matrix[i][j] = cur_node * -1
