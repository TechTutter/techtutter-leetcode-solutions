from solution import Solution, TreeNode

class TestSolution:
    def test_1(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        assert s.isSymmetric(root) == True
        
    def test_2(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)
        assert s.isSymmetric(root) == False