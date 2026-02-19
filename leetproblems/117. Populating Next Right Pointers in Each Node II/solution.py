# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

class Solution:
    def connect(self, root: Node) -> Node:
        """
        - iterate with BFS level by level, storing a "level" queue for current level
        - for len(queue), set prev.next to current node
            - Use initial dummy node for prev to avoid None nodes issues
        """

        if root is None:
            return root

        queue = deque([root])
        while queue:
            prev = Node()
            for _ in range(len(queue)):
                curr = queue.popleft()
                left, right = curr.left, curr.right
                prev.next = curr
                prev = curr
                
                if left: queue.append(left)
                if right: queue.append(right)
        
        return root
