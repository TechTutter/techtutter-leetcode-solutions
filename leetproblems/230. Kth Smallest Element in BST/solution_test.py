from solution import Solution, TreeNode

class TestSolution:
    def test_testcase1(self):
        s = Solution()
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        assert s.kthSmallest(root, 1) == 1

    def test_testcase2(self):
        s = Solution()
        root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
        assert s.kthSmallest(root, 3) == 3
