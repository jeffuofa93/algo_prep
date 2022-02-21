# Yield command 

- Uses a generator instead of a list so it just stores the last value to compute the next one 
```python
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for x in nums:
            if nums[abs(x)-1] < 0:
                yield abs(x)
            else:
                nums[abs(x)-1] *= -1
```
```python
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                result.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return result
```
- the first function returns a generator instead of a list 
- this generator just contains the ability to get the next value from the position of the last yield statement instead
of storing an entire new list in memory 

