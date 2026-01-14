from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """
        do DFS on root.left, store visited nodes in queue including None
        do DFS_right on root.right, pop from queue and if a value is different is not symmetric
        """        
        visited = self.dfs_left(root.left)
        queue = self.dfs_right(root.right, visited)
        
        return len(visited) == 0 and len(queue) == 0

    def dfs_left(self, root: TreeNode | None) -> deque[TreeNode | None]:
        queue = deque([root])
        visited = deque([])

        while queue:
            node = queue.pop()
            if node:
                queue.append(node.right)
                queue.append(node.left)
            visited.append(node.val if node else None)
        return visited

    def dfs_right(self, root: TreeNode | None, visited) -> deque[TreeNode | None]:
        queue = deque([root])

        while queue and visited:
            node = queue.pop()
  
            right_val = node.val if node else None
            left_val = visited.popleft()

            if left_val != right_val:
                return [None]
            elif node:
                queue.append(node.left)
                queue.append(node.right)
        print(queue)
        return queue

s = Solution()
root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
print(s.isSymmetric(root))
