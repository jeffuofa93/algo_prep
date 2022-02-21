# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        stack = []
        cur = head
        while cur is not None:

            stack.append(cur)
            cur = cur.next
        root = stack.pop()
        root.next = None
        cur = root
        while stack:
            node = stack.pop()
            node.next = None
            cur.next = node
            cur = cur.next
        return root
