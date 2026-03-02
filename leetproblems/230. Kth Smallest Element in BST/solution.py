class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        step = 1
        def dfs(root):
            if root is None: return 0

            sum1 = dfs(root.left)

            nonlocal step
            curr = 0 if step != k else root.val
            step += 1

            sum2 = dfs(root.right)
            return sum1 + curr + sum2 
    
        return dfs(root) 