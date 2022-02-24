from collections import Counter
from typing import List


def performOperations(arr: List[int], operations):
    for start, end in operations:
        subSection = arr[start:end].reverse()
        for i in range(start, end):
            arr[i] = subSection[i]
    return arr


def ceiling(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return arr[mid]
        if arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return arr[lo]


x = [2, 3, 5, 9, 14, 16, 18]
target = 8

z = [2, 3, 5]

cX = Counter(x)
dx = Counter(z)
y = cX - dx
print(y)
print(dx)
