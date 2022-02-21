# Sliding Window Notes

## Overview

- Used for finding subarrays in an array that satisfy given conditions
- Maintain a subset of items as your window and resize and move that window within the larger list until you find a
  solution
- Maintain a subset of items as your window and resize and move that window within the larger list until you find a solution 
- Subset of Dynamic Programming 
- Time complexity **O(N) = linear time**
- Space complexity: **O(1) = constant space**
- You can identify Sliding Window problems amongst subarray/substring related questions 

## Example: Find the subarrays that add up to 9 

- input = [1,2,3,4,5,6,7,8,9]
- start with two element window [1,2], to small so we grow window 
- [1,2,3] still small so grow window again 
- [1,2,3,4] window too big 10 so we shrink window from the left
- [2,3,4] - found valid subarray now we continue to shrink if the window is too large and grow if it is too small 

## Example: Given an array of integers, find the maximum sum sub of the required size 

- ex input = [-1,2,3,1,-3,2]    sub array size = 2
- start we have [-1,2] that gives us a max of 1 

- Interview Tips 
  - Requirments
    - Analyze the requirments even in simple questions , they might not be so simple
    - Subarrays are contigous by defininition, so the elements should be adjacent 
    - Input size could be anything
  - Analysis
    - Input size is unlimited so memory can blow up if we are not careful of what we keep in memory
      - Do not pre-calculate and store all possible variations before hand (brute force)
      - Do not use recursion call stack with overflow 
    - Think through data structures that can be utilized

- Brute force approach 
  - Caclulate all possible sub arrays with 2 members and store them in a hashtable 
  - Iterate over the hash table until you find the subarray with the max sum
  - Time complexity O(n) for creation, O(1) every lookup afterwards
  - Space complexity: O(n) - very bad 
- Sliding Window 
  - Calculate first two elements, slide the window by one element at a time only storing the max 
  - Time complexity O(n)
  - Space complexity O(1)

## Kadanes Algorithm 

- Maximum Sub Array Problem 
```python
def kadane(arr):
    maxCurrent = maxGlobal = arr[0]
    for i in range(1,len(arr)):
        maxCurrent = max(arr[i],maxCurrent+arr[i])
        if maxCurrent > maxGlobal:
            maxGlobal = maxCurrent
    return maxGlobal
```

## Minimum Size array 

- idea is to keep a left and right pointer and move right if total < target and move left if total >= target
- also must decrement total and update minLength while total >= target
```python
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left,total = 0,0
    minLength = float("inf")
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            minLength = min(right - left + 1,minLength)
            total -= nums[left]
            left +=1 
            
    return 0 if minLength == float("inf") else minLength
```

