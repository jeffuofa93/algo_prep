"""
If we are dfsing we need to grab a node and for each element in the children array we dfs on that child
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        if not self.children:
            return
        for node in self.children:
            node.depthFirstSearch(array)
        return array
