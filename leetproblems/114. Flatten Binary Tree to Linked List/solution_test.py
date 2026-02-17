from solution import Solution, TreeNode

class TestSolution:
    def test_flatten(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
        Solution().flatten(root)
        expected = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))))
        assert root == expected