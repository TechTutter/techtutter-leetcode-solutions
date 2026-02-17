# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # move a node by n spots
        dummy = ListNode(0, head)
        prev = dummy
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        # get n-th node from end
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next else None 

        return dummy.next
