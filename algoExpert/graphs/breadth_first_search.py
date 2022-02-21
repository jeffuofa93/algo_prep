"""
breadth first search of each children

we take out start node and add it to the queue then while our queue is not empty we add pop off the most recent
element from the queue and adds all it's children
"""
from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        q = deque()
        q.append(self)
        while q:
            cur_node = q.popleft()
            array.append(cur_node.name)
            for node in cur_node.children:
                q.append(node)
        return array
