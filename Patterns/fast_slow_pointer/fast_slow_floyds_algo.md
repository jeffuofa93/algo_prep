# Fast and Slow pointer Floyd's Cycle Detection 

## Linked List Cycle 

- To detect where a cycle starts in a linked list we use a Fast and Slow pointer 
- The fast pointer moves by 2 nodes and the slow pointer moves by 1 node 
- When the fast and slow pointer meet we leave 1 pointer at the point of intersection and then we create a new slow pointer from the start
- We then move our slow pointer at the start and the intersection pointer 1 at a time until they meet and this is the beginning of the cycle 
- The Floyd theorem says that the distance from the first point of intersection to the start of the cycle is always the same as the distance from the 
start of the linked list to the start of the cycle 

## Ex: 287 Find Duplicate Number 
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0;
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
```




