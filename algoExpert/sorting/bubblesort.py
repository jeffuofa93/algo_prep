def bubbleSort(array):
    for i in range(len(array)):

        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
    return array


z = [1, 3, -5, 4, 12, -2]
print(bubbleSort(z))
