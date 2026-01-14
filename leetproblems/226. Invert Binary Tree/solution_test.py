from solution import Solution, TreeNode

class TestInvertTree:
    def test_testcase1(self):
        s = Solution()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        assert s.printTree(s.invertTree(root)) == [4,7,2,9,6,3,1]

    def test_testcase2(self):
        s = Solution()
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        assert s.printTree(s.invertTree(root)) == [2,3,1]
