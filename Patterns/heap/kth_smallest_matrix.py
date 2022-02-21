from heapq import heappop, heappush
from typing import List


class Solution:  # 204 ms, faster than 54.32%
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        minHeap = []  # val, r, c
        for r in range(min(k, m)):
            print(f"r={r} matrix val = {matrix[r][0]}")
            heappush(minHeap, (matrix[r][0], r, 0))

        ans = -1  # any dummy value
        for i in range(k):
            ans, r, c = heappop(minHeap)
        if c + 1 < n:
            heappush(minHeap, (matrix[r][c + 1], r, c + 1))

        return ans


sol = Solution()
x = [[1, 3, 7], [5, 10, 12], [6, 10, 15]]

sol.kthSmallest(x, 4)
