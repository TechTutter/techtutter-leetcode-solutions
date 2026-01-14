# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeRecursive(root)
        return root

    def invertTreeRecursive(self, node: TreeNode | None) -> TreeNode | None:
        if node is None:
            return
        
        self.invertTreeRecursive(node.left)
        self.invertTreeRecursive(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

    def printTree(self, node: TreeNode | None) -> list[int]:
        if node is None:
            return []
        values = []
        nodes = [node]
        while nodes:
            node = nodes.pop(0)
            values.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return values
