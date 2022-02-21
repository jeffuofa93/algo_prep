
"""
take a sorted array and return  new array that is the squares sorted

what do we know

basic case where all nums positive it's just squaring

With negatives we know that as we go from left to right if the number is positive it just goes into the next slot but
if the number is negative it becomes the first element so my thought process is either A use a deque and append negative
numbers to the front a
"""


def sortedSquaredArray(array):
