from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        children_p = deque([p])
        children_q = deque([q])

        while children_p and children_q:
            next_p = children_p.popleft()
            next_q = children_q.popleft()
            
            if next_p and next_q:
                if next_p.val == next_q.val:
                   children_p.extend([next_p.left, next_p.right])
                   children_q.extend([next_q.left, next_q.right])
                else:
                    return False
            
            if bool(next_p) ^ bool(next_q):
                return False
            
        return not children_p and not children_q
        