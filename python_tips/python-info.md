# Information about Python

## Collections

- defaultdict
- add by writing from collections import defaultdict
- intialize with new_dict = defailtdict("type of values")

 ```python 
 from collections import defaultdict 

 def_dict = defaultdict(list)
 reg_dict = {}
 ```

- advantages is that we don't have to intalize the list or other collection in the list and it will never throw a key
  error it just adds the element

## How to sort using a key

```python
intervals = [[0, 20], [1, 15], [7, 1]]
intervals.sort(key=lambda i: i[1])
```

## Zip function

- the zip function takes two or more collections and tuples the elements together to be used in any other
  comparisions/operations
- Example below

```python
from collections import defaultdict

usernames = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
timestamps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
websites = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]

users = defaultdict(list)
for user, time, site in sorted(zip(usernames, timestamps, websites), key=lambda x: (x[0], x[1])):
    users[user].append(site)
```

## Yield command

- Uses a generator instead of a list so it just stores the last value to compute the next one

```python
from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    for x in nums:
        if nums[abs(x) - 1] < 0:
            yield abs(x)
        else:
            nums[abs(x) - 1] *= -1
```

```python
from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    result = []
    for x in nums:
        if nums[abs(x) - 1] < 0:
            result.append(abs(x))
        else:
            nums[abs(x) - 1] *= -1
    return result
```

- the first function returns a generator instead of a list
- this generator just contains the ability to get the next value from the position of the last yield statement instead
  of storing an entire new list in memory

## Dictionary Comprehension Example Flatten Dictionary

- code creates key with if else in first line then iterates through both the items of current dict and of the next 
  recursive call 
- if else at buttom seperates the two results 
```python
def flattenDict(dictElement, separator="_", prefix=""):
    return (
        {
            prefix + separator + k if prefix else k: v
            for kk, vv in dictElement.items()
            for k, v in flattenDict(vv, separator, kk).items()
        }
        if isinstance(dictElement, dict)
        else {prefix: dictElement}
    )
```