from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    """
    Visit one level at once. When the entire level is visited, increment the height.
    """
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = deque([root])
        height = 0
        nodes_at_level = 1

        while queue:
            curr = queue.popleft()
            nodes_at_level -= 1

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            if nodes_at_level == 0:
                height += 1
                nodes_at_level = len(queue)

        return height