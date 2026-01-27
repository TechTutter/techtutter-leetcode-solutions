from solution import Solution, TreeNode

class TestExerciseName:
    def test_testcase1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)

        assert Solution().countNodes(root) == 6

