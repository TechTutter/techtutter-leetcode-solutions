from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return []

        queue = deque([root])
        while queue:
            res.append([])
            for _ in range(len(queue)):
                curr = queue.popleft()
                left, right = curr.left, curr.right
                if left: queue.append(left)
                if right: queue.append(right)
                res[-1].append(curr.val)
        return res
        