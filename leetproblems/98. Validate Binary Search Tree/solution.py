from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        a node is valid if is between left and right boundaries
        use parent either as left or right when descending
        '''

        def isValid(root, left, right):
            if root is None:
                return True

            return root.val > left and root.val < right and isValid(root.left, left, root.val) and isValid(root.right, root.val, right)
        return isValid(root, -float('inf'), float('inf'))