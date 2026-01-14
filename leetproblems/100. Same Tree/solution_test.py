from solution import Solution, TreeNode 

class TestIsSameTree:
    def test_testcase1(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        assert Solution().isSameTree(p, q) == True

    def test_testcase2(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        q = TreeNode(1)
        q.right = TreeNode(2)
        assert Solution().isSameTree(p, q) == False

    def test_testcase3(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)
        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        assert Solution().isSameTree(p, q) == False