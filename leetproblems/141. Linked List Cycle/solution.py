# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        fast = head
        slow = ListNode(0)
        slow.next = head
        while fast:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
        return False
