"""
Plan
take values and add the difference between them

10 and 7

target 17



"""


def twoSum(array, targetSum):
    diffVals = {}
    for i in array:
        diff = targetSum - i
        if i in diffVals:
            return [i, diffVals[i]]
        diffVals[diff] = i
    return []


arr = [3, 5, -4, 8, 11, 1, -1, 6]
tar = 10
print(twoSum(arr, tar))
