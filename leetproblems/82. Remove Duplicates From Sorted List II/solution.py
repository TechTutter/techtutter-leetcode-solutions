# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(math.inf, head)
        prev = dummy
        curr = dummy.next

        while curr:
            next_val = curr.next.val if curr.next else None
            if next_val is not None and curr.val == next_val:
                while next_val is not None and curr.val == next_val:
                    curr.next = curr.next.next
                    next_val = curr.next.val if curr.next else None
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
 

        