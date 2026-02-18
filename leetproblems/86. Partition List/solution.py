class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        """
        - create 3 new lists lower_nodes, equal_nodes, greater_nodes
        - from head onward, append each node to the corresponding list. this preserves relative order! when appending the node, store the "next" value, and set curr.next to None.
        - when list is done, append head of equal_nodes to tail of lower_nodes, and head of greater_nodes to tail of equal_nodes
        """
        if head is None or head.next is None:
            return head

        lower_nodes = ListNode(0)
        greater_equal_nodes = ListNode(0)

        lower = lower_nodes
        greater_equal = greater_equal_nodes

        lower_tail = None

        curr = head
        while curr:
            if curr.val < x:
                lower.next = curr
                curr = curr.next
                lower = lower.next
                lower_tail = lower
                lower.next = None
            else:
                greater_equal.next = curr
                curr = curr.next
                greater_equal = greater_equal.next
                greater_equal.next = None        
        
        
        if lower_tail is not None:
            lower_tail.next = greater_equal_nodes.next

        if lower_nodes.next is not None:
            return lower_nodes.next
        else:
            return greater_equal_nodes.next

        
        