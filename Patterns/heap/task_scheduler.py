from typing import List
from heapq import heappush, heappop


from heapq import heappush, heappop
from collections import Counter


def leastInterval(tasks, n):
    curr_time, heap = 0, []
    for k, v in Counter(tasks).items():
        heappush(heap, (-1 * v, k))
    print(heap)
    while heap:
        i, temp = 0, []
        while i <= n:
            curr_time += 1
            if heap:
                x, y = heappop(heap)
                if x != -1:
                    temp.append((x + 1, y))
            if not heap and not temp:
                break
            else:
                i += 1
        for item in temp:
            heappush(heap, item)
    return curr_time


x = ["A", "A", "A", "A", "B", "C", "D", "E"]
n = 2
print(leastInterval(x, n))
