def flatten_dict(entryDict, separator=".", prefix=""):
    temp = {}
    if isinstance(entryDict, dict):
        for kk, vv in entryDict.items():
            for k, v in flatten_dict(vv, separator, kk).items():
                temp[prefix + separator + k] = v
        return temp
    else:
        temp[prefix] = entryDict
        return {prefix: entryDict}


def flattenDict(dictElement, separator="_", prefix=""):
    return (
        {
            prefix + separator + k if prefix else k: v
            for kk, vv in dictElement.items()
            for k, v in flatten_dict(vv, separator, kk).items()
        }
        if isinstance(dictElement, dict)
        else {prefix: dictElement}
    )


ini_dict = {
    "geeks": {"Geeks": {"for": 7}},
    "for": {"geeks": {"Geeks": 3}},
    "Geeks": {"for": {"for": 1, "geeks": 4}},
}

print("final_dictionary", str(flatten_dict(ini_dict)))


def array_of_array_products(arr):
    """
    [8,10,2]
    prev = [1,8,80]

    next = [20,2,1]

    i = 0
    result = [20,16,80]

    Time = O(n)

    Space = O(3n)

    """
    if len(arr) == 1:
        return []

    prev = [1]
    total = 1
    for i in range(len(arr) - 1):
        total *= arr[i]
        prev.append(total)

    nxt = [1]
    total = 1
    #
    for i in range(len(arr) - 1, 0, -1):
        total *= arr[i]
        nxt.append(total)
    nxt.reverse()

    result = []
    for i in range(len(arr)):
        result.append(prev[i] * nxt[i])
    return result


arr = [8, 10, 2]
arr1 = [2, 7, 3, 4]
print(array_of_array_products(arr))
print(array_of_array_products(arr1))

# feedback state the problem back
