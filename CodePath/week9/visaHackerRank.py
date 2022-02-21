"""
Umpire
Understand we are given a target and then we need to find the distance from the
Idea keep searching in left and right direction and return the min
"""

# def toolchanger(tools, startIndex, target):
#     leftMoves = rightMoves = 0
#     leftIndex = rightIndex = startIndex
#     endIndex = len(tools) -1
#     while True:
#         leftIndex = swapIndex(leftIndex,endIndex)
#         rightIndex = swapIndex(rightIndex,endIndex)
#         leftIndex-=1
#         rightIndex+=1
#         leftMoves+=1
#         rightMoves+=1
#         if tools[leftIndex] == target:
#             return leftMoves
#         if tools[rightIndex] == target:
#             return rightIndex
#
#
# def swapIndex(curIndex,toolsLength):
#     if curIndex >= toolsLength:
#         return 0
#     if curIndex == 0:
#         return toolsLength
#     return curIndex
#
#
# def stockPairs(stocksProfit, target):
#     solutions = set()
#     beenSeen = set()
#     numberOfPair = 0
#     for i,num in enumerate(stocksProfit):
#         if num in solutions and num not in beenSeen:
#             numberOfPair += 1
#             beenSeen.add(target-num)
#             beenSeen.add(num)
#         elif num not in solutions:
#             solutions.add(num)
#     return numberOfPair

# HW1
# count = 0
# for i in range(1,100):
#     for j in range(1,100):
#         count+=1
# print(count)

# # HW2
# count = 0
# i = 0
# while i < 100:
#     j = 0
#     while j < i:
#         count+=1
#         j+=1
#     i+=1
# print(count)

#HW3
def hw3():
    count = 0
    i = 1
    while i <= 1024:
        print(f'i={i}')
        j = i
        while j > 0:
            print(f'j={j}')
            count += 1
            j-=1
        print("j ends")
        i = i *2
    print(f'count = {count} \n')

#
# hw3()

# hw4
def hw4():
    count = 0
    for i in range(2*100):
        j = 1
        jcount = 0
        while j <= i:
            print(f'j={j}')
            count +=1
            j = j *2
            jcount+=1
        print(f'# of times j ran this loop {jcount}')
    print(f'count = {count} \n')

#hw7


def hw7(arr):
    count = 0
    for i in range(len(arr)-1):
        j = i +1
        while j>0 and arr[j] > arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j-=1
            count +=1
            print(arr)
        print()
    print(count)

hw7([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

"""
This program sorts an array in descending order so [1,4,2,3,5] becomes [5,4,3,2,1]. The program does this by iterating
over the array and for each value moving it left in the array until the element to its left is >= to it  

B - 

If the array is already sorted in descending order then count is equal to 0. Worst case is the array is sorted in 
ascending order which would be O(n^2) count would be n^2/2
"""