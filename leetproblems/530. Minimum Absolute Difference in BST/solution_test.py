from solution import Solution, TreeNode

class TestSolution():
    def test_testcase1(self):
        s = Solution()
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
        assert s.getMinimumDifference(root) == 1

    def test_testcase2(self):
        s = Solution()
        root = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
        assert s.getMinimumDifference(root) == 1