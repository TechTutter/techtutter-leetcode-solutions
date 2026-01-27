from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if root is None: return []

        queue = deque([root])
        res = []

        while queue:
            level = len(queue)
            level_sum = 0

            for _ in range(level):
                node = queue.popleft()
                if node is not None:
                    level_sum += node.val
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
            res.append(level_sum / level)
        
        return res