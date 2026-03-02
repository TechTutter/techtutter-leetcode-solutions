class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        """
        base case ->
          build Node n from preorder_index
          n.left will be preorder_index+1
          n.right will be preorder_index+2

        we just need to make sure, using inorder, that left and right are not inverted

        """
        index = {v: i for i, v in enumerate(inorder)}
        preorder_index = 0
        
        def helper(prev_left, prev_right):
            if prev_left > prev_right:
                return None
            
            nonlocal preorder_index
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1
            
            inorder_index = index[root_val]
            
            root.left = helper(prev_left, inorder_index - 1)
            root.right = helper(inorder_index + 1, prev_right)
            
            return root
        
        return helper(0, len(inorder) - 1)

s = Solution()

def print_tree_inorder(root):
    if not root:
        return []
    return print_tree_inorder(root.left) + [root.val] + print_tree_inorder(root.right)

def print_tree_preorder(root):
    if not root:
        return []
    return [root.val] + print_tree_preorder(root.left) + print_tree_preorder(root.right)

print(print_tree_inorder(s.buildTree([3,9,20,15,7], [9,3,15,20,7])))
print(print_tree_preorder(s.buildTree([3,9,20,15,7], [9,3,15,20,7])))