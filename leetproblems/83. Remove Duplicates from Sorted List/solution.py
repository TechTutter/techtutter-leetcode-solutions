class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: "ListNode | None") -> "ListNode | None":
        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next