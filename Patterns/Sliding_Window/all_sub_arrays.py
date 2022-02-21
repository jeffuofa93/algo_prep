"""
Problem find all sub arrays that add up to the given sum

Edge cases: List is empty,

Ex input - [1,7,4,3,1,2,1,5,1], desired sum = 7

What do you want returned for the result each index or just the gap say (4-6)

Idea we iterate through the array starting at size 1 and if the current array is too small we grow to the right if
the current array is too big we shrink from the left

if current window is 1 element instead of shrinking left we just jump to next right element
"""

def all_sub_arrays(arr,sum):
    result = []
    i = 0
    cur_arr = set()
    while i < len(arr)-1:
