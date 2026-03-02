class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        postorder_index = len(postorder) - 1
        index = {v: i for i, v in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None

            nonlocal postorder_index
            root_val = postorder[postorder_index]
            root = TreeNode(root_val)
            postorder_index -= 1

            inorder_index = index[root_val]

            root.right = helper(inorder_index +1, right)
            root.left = helper(left, inorder_index - 1)

            return root

        return helper(0, len(inorder) - 1)
        