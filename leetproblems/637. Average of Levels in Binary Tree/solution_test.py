from solution import Solution, TreeNode


class TestExerciseName:
    def test_testcase1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        assert Solution().averageOfLevels(root) == [3.0, 14.5, 11.0]

    def test_testcase2(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.left.left = TreeNode(15)
        root.left.right = TreeNode(7)
        assert Solution().averageOfLevels(root) == [3.0, 14.5, 11.0]
        