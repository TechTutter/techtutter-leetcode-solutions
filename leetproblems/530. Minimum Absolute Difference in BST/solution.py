class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode | None) -> int:
        dummy = TreeNode(float("inf"), root)
        state = {
            "prev": dummy,
            "min": float('inf')
        }

        def dfs(root):
            if root is None: return

            dfs(root.left)
            state["min"] = min(state["min"], abs(state["prev"].val - root.val))
            state["prev"] = root
            dfs(root.right)
    
        dfs(root)
        return state["min"]