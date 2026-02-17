# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 0 or head is None:
            return head

        curr = tail = head
        n = 0
        while curr:
            n += 1
            tail = curr
            curr = curr.next

        r = k % n
        if r == 0 or n == 1:
            return head

        # get starting point to rotate
        slow = fast = head
        for _ in range(r+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next

        tail.next = head
        head = slow.next
        slow.next = None

        return head
        