class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        left_boundary = dummy
        
        # Find left node
        for _ in range(left - 1):
            left_boundary = left_boundary.next
        
        # Reverse
        left_node = left_boundary.next
        curr = left_node
        prev = None
        
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Adjust remaining pointers
        
        new_head_sublist = prev
        right_boundary = curr
        left_boundary.next = new_head_sublist
        left_node.next = right_boundary
        
        return dummy.next