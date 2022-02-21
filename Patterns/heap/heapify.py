# max heapify
def heapify(A, i):
    largest = i
    leftChild = 2 * i
    rightChild = 2 * i + 1

    if leftChild < heapsize(A) and A[leftChild] > A[largest]:
        largest = leftChild

    if rightChild < heapsize(A) and A[rightChild] > A[largest]:
        largest = rightChild

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest)


def heapsize(A):
    return 1


