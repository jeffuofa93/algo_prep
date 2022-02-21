# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    if linkedList is None:
        return
    d_head = LinkedList("dummy")
    d_head.next = linkedList
    p = d_head
    cur = linkedList
    while cur and cur.next:
        if cur.value == p.value:
            p.next = cur.next
            cur = cur.next

        p = cur
        cur = cur.next
    return d_head.next
