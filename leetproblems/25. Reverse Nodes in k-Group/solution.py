from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or head is None:
            return head
            
        dummy = ListNode(0, head)

        n = 0
        curr = dummy.next
        while curr:
            n += 1
            curr = curr.next

        loops = n // k

        prev_section_tail = dummy
        prev = dummy
        curr = dummy.next
        for _ in range(loops):
            section_head = curr # first section node - 3
            for _ in range(k):
                nxt = curr.next # next - 3
                curr.next = prev # swap - 1
                prev = curr # 2
                curr = nxt # 3
            prev_section_tail.next = prev # 2
            prev_section_tail = section_head # 1
            section_head.next = curr # 3

        return dummy.next

            