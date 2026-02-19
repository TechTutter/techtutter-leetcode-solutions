# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Suboptimal solution, it's O(n^2)
        There is only 2 ways a node can be used in a path because of nature of a tree
            - can be a root of the subtree forming the path
            - can be a simple node in the path
        explore all nodes, each node will act as the root of the current subpath we are epxloring
        recursively get the better path as max(left, right) children for the subtree currently analyzing
        if the obtained path is greater then current global max, store it
        """
        res = -float('inf')
        def depth_max_path(root: TreeNode | None):
            if root is None:
                return 0
            
            return max(0, root.val + max(depth_max_path(root.left), depth_max_path(root.right)))

        queue = [root]
        while queue:
            curr = queue.pop()
            left, right = curr.left, curr.right
            res = max(res, curr.val + depth_max_path(left) + depth_max_path(right))
            if left: queue.append(left)
            if right: queue.append(right)

        return res if res != -float('inf') else 0