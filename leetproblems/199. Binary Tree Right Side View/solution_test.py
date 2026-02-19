from typing import List, Optional
from collections import deque
from solution import Solution, TreeNode


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
            
    return root


class TestSolution:
    def test_example1(self):
        root = build_tree([1, 2, 3, None, 5, None, 4])
        assert Solution().rightSideView(root) == [1, 3, 4]
    
    def test_example2(self):
        root = build_tree([1, 2, 3, 4, None, None, None, 5])
        assert Solution().rightSideView(root) == [1, 3, 4, 5]
        
    def test_example3(self):
        root = build_tree([1, None, 3])
        assert Solution().rightSideView(root) == [1, 3]
        
    def test_example4(self):
        root = build_tree([])
        assert Solution().rightSideView(root) == []

