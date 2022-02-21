


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree, target, closest=float("inf")):
    if tree is None:
        return closest
    if abs(tree.value - target) < abs(target - closest):
        closest = tree.value
    return min(findClosestValueInBst(tree.left, target, closest),findClosestValueInBst(tree.right,target,closest))

