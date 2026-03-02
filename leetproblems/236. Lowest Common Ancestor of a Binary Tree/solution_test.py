from solution import Solution, TreeNode

class TestSolution:
    def test_testcase1(self):
        s = Solution()
        root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
        p = root.left
        q = root.right
        assert s.lowestCommonAncestor(root, p, q) == root

    def test_testcase2(self):
        s = Solution()
        root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
        p = root.left
        q = root.left.right.right
        assert s.lowestCommonAncestor(root, p, q) == root.left

    def test_testcase3(self):
        s = Solution()
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        p = root.left
        q = root.right
        assert s.lowestCommonAncestor(root, p, q) == root