
from solution import Solution, TreeNode


class TestExerciseName:
    def test_testcase1(self):
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n1.left = n2
        n1.right = n3
        assert Solution().maxPathSum(n1) == 6

    def test_testcase2(self):
        n1 = TreeNode(-10)
        n2 = TreeNode(9)
        n3 = TreeNode(20)
        n4 = TreeNode(15)
        n5 = TreeNode(7)
        n1.left = n2
        n1.right = n3
        n3.left = n4
        n3.right = n5
        assert Solution().maxPathSum(n1) == 42

