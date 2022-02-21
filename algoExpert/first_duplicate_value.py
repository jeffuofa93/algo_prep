def firstDuplicateValue(array: list[int]) -> int:
    """
    Idea is we iterate through the array and because each elemenet is in range n we make the index of the element negative
    and absolute val everything we take out of the array. Then if we see an element and it's index is already negative
    we know we have seen it before
    """
    for value in array:
        abs_val = abs(value)
        if array[abs_val - 1] < 0:
            return abs_val
        array[abs_val - 1] *= -1
    return -1


def firstDuplicateValue1(array: list[int]) -> int:
    """
    intial idea, traverse the array adding each element to a set if you encounter an element that already exists in the
    set return that element
    """
    visited = set()
    for i in array:
        if i in visited:
            return i
        visited.add(i)
    return -1


x = [2, 1, 3, 4, 1]
# some way to move elements so I can check for a duplicate
for i in range(10):
    print("test")

    
