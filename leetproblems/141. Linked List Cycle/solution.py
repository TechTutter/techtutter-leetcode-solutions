# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        visited = set()

        next_node = head
        while next_node:
            if next_node in visited:
                return True
            else:
                visited.add(next_node)
                next_node = next_node.next
        return False
