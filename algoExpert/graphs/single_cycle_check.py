"""
We have to visit every element in the array exactly once
If we revisit our start before we visit every node we it's false otherwise we
"""


def hasSingleCycle(array):
    num_visited = 0
    cur_idx = 0
    while num_visited < len(array):
        if num_visited > 0 and cur_idx == 0:
            return False
        num_visited += 1
        cur_idx = getNextIdx(cur_idx, array)
    return cur_idx == 0


def getNextIdx(cur_idx, array):
    jump = array[cur_idx]
    next_idx = (cur_idx + jump) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)
