from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not other or not isinstance(other, TreeNode):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        
        queue = deque([])
        curr = root
        while curr:
            # store right and replace it with left
            left, right = curr.left, curr.right
            if right: 
                queue.append(right)
                curr.left = None
            
            # pick next node
            if left:
                curr.right = left
            else:
                n = queue.pop() if queue else None
                curr.right = n

            curr = curr.right
                