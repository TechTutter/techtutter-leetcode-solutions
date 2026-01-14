from solution import Solution, TreeNode 

class TestMaxDepth:
    def test_testcase1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        assert Solution().maxDepth(root) == 3

    def test_testcase2(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        assert Solution().maxDepth(root) == 2
        
