"""
we intialize a max value to neg infinity
check at the starting sub array if the max is greater then cur max we set the new max then we move to the right
"""


def max_sub_array(arr, size):
    max_val = float("-inf")
    max_pair = None
    for i in range(len(arr) - (size - 1)):
        cur_sum = 0
        for j in range(size):
            cur_sum += arr[i + j]
        if cur_sum > max_val:
            max_val = cur_sum
            max_pair = [arr[i], arr[i + 1]]
    return max_pair

x = [-1,2,3,1,-3,2]
print(max_sub_array(x,3))