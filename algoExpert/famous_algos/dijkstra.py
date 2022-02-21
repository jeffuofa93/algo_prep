import itertools
from heapq import *


def dijkstrasAlgorithm(start, edges):
    num_vertices = len(edges)

    # Write your code here.
    visited = set()
    min_distances = [float("inf") for _ in range(num_vertices)]
    min_distances[start] = 0
    min_distance_heap = MinHeap([(idx, float("inf")) for idx in range(num_vertices)])
    min_distance_heap.update(start, 0)
    min_distances[start] = 0

    while not min_distance_heap.isEmpty():
        vertex, cur_min_dist = min_distance_heap.remove()

        if cur_min_dist == float("inf"):
            break
        for edge in edges[vertex]:
            destination, dist_destination = edge
            new_dist = cur_min_dist + dist_destination
            cur_dest_dist = min_distances[destination]
            if new_dist < cur_dest_dist:
                min_distances[destination] = new_dist
                min_distance_heap.update(destination, new_dist)
    return list(map(lambda x: -1 if x == float("inf") else x, min_distances))


class MinHeap:
    def __init__(self, array):
        self.vertex_map = {idx: idx for idx in range(len(array))}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
