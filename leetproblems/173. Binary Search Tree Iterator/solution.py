# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.idx = 0
        self.size = 0
        self.values = []

        def dfs(root):
            if root is None:
                return
            
            left, right = root.left, root.right
            dfs(root.left)
            self.size += 1
            self.values.append(root.val)
            dfs(root.right)
        
        dfs(root)
        

    def next(self) -> int:
        curr = self.idx
        self.idx += 1
        return self.values[curr]
        
    def hasNext(self) -> bool:
        return self.idx < self.size
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()