# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: "ListNode | None") -> "ListNode | None":
        
        def merge_sort(head):
            if not head or not head.next:
                return head
            
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            mid = slow.next
            slow.next = None  # split
            
            left = merge_sort(head)
            right = merge_sort(mid)
            return merge(left, right)

        def merge(left: "ListNode | None", right: "ListNode | None") -> "ListNode | None":
            dummy = ListNode(0)
            head = dummy
            while left and right:
                if left.val <= right.val:
                    head.next = left
                    left = left.next
                else:
                    head.next = right
                    right = right.next
                head = head.next
                
            head.next = left or right
            return dummy.next

        return merge_sort(head)