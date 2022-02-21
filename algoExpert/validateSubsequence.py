"""
idea use a pointer

so we start two pointer one at the start of the array and one at the start of the sequence
every time we find a value in the array we increment both the sequence and the array pointer
if the sequence pointer equals the array length we return true else we return false at the end
"""


def isValidSubsequence(array, sequence):
    seq = 0
    for i in range(len(array)):
        if array[i] == sequence[seq]:
            seq += 1
        if seq == len(sequence):
            return True
    return False


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 11]
print(isValidSubsequence(array, sequence))
