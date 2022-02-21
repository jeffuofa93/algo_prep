# Backtracking Overview 

1. Make Choices 
2. Constraints on Choices
3. Goal 

## Example Sudoko 

- each cell we can choose a number 1 through 9 
- 

## Three types of backtracking 

- Permutations - all possible orderings of elements must equal the length of the original input 
can allow or disallow duplicates. Ordering matters "ABC", "BCA" different 
- Combinations - all possible combinations of elements where different orders are not unique but duplicates allowed
- Subset - combinations but no duplicate elements allowed

```python
"""
With subsets we cannot have duplicates so once we select from a position we cannot go back to that positon
why i+1 and loop from i

Also we want to capture at each valid call so we append to result each call
"""


def subsets(nums):
    size = len(nums)
    result = []

    def backtrack(pos, sub):
        if pos >= size:
            result.append(sub.copy())
            return
        result.append(sub.copy())
        for i in range(pos, size):
            sub.append(nums[i])
            backtrack(i + 1, sub)
            sub.pop()

    backtrack(0, [])
    return result

"""
we only add once we reach required size 
we do not select the same element more then once
"""
def permutations(nums):
    size = len(nums)
    result = []
    def backtrack(perm):
        if len(perm) >= size:
            result.append(perm.copy())
        for i in range(size):
            if nums[i] in perm:
                continue
            perm.append(nums[i])
            backtrack(perm)
            perm.pop()


```


## LC 90 Subsets 2

- Big idea is that to prevent duplicates in the subset we can to regular backtrack where we select the next element 
  then for our loop instead of automatically taking the elements we skip any items that are the same as the other 
  branch will already find all subsets


## LC 46 Permutations

- Got good solution but was checking entire list each for loop 
- TRICK - we can move the current element we are at in our permuatation to the front of the list to move past it 
```python
class Solution:
    def permute(self, nums):
        result = []
        size = len(nums)
        def backtrack(start,perm):
            if start >= size:
                result.append(perm.copy())
                return
            for i in range(start,size):
                nums[start],nums[i] = nums[i],nums[start]
                backtrack(start+1,perm+[nums[start]])
                nums[start],nums[i] = nums[i],nums[start]
                
        backtrack(0,[])
        return result
```

## LC 47 Permutations 2
- TRICK - think of each unqiue element as a choice instead of the element 
- Use dictionary, in loop iterate over dictionary where count of element > 0 
- on select decrement count , increment after

