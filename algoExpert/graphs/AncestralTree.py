"""
my idea
we know that a common ancestor has to be at or above the height of the tallest node because we start from the botttom
My idea is we determine which node is deeper in the tree
Then we move the deepest node up to the level of the shallower node and check if the shallow node is the ancestor
then each time we move both nodes up the tree and check if they have the same ancestor
then we build a set of ancestors for each node
"""


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(
    topAncestor: AncestralTree,
    descendantOne: AncestralTree,
    descendantTwo: AncestralTree,
):
    if topAncestor.name == descendantOne.name or topAncestor.name == descendantTwo.name:
        return topAncestor
    one_height = find_height(descendantOne)
    two_height = find_height(descendantTwo)

    if one_height < two_height:
        deep_node, short_node = descendantTwo, descendantOne
        short_height, deep_height = one_height, two_height
    else:
        deep_node, short_node = descendantOne, descendantTwo
        short_height, deep_height = two_height, one_height
    while deep_height > short_height:
        deep_node = deep_node.ancestor
        deep_height -= 1
    if short_node.name == deep_node.ancestor:
        return short_node
    while (
        short_node.ancestor is not None
        and deep_node.ancestor is not None
        and short_node.name != deep_node.name
    ):
        short_node = short_node.ancestor
        deep_node = deep_node.ancestor
    return short_node


def checkAncestor(deep, short):
    return (
        short.name == deep.ancestor
        or deep.name == short.ancestor
        or deep.ancestor == short.ancestor
    )


def find_height(node: AncestralTree):
    if node is None:
        return 0
    return 1 + find_height(node.ancestor)
