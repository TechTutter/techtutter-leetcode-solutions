# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, curr: int) -> int:
            if node is None:
                return 0

            curr = curr * 10 + node.val

            if node.left is None and node.right is None:
                return curr

            return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)

        