from typing import List


def threeNumberSum(array: list[int], targetSum: int) -> list[list[int]]:
    """
    Big take away you sort the list and the check each element infront of the
    current and move left if the total is to big and move right if too small

    :param array:
    :param targetSum:
    :return:
    """
    array.sort()
    triplets: list[list[int]] = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            cur_sum = array[i] + array[left] + array[right]
            if cur_sum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif cur_sum < targetSum:
                left += 1
            elif cur_sum > targetSum:
                right -= 1
    return triplets
