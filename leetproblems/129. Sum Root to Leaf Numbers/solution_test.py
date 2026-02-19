from solution import Solution, TreeNode

class TestSolution():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().sumNumbers(root) == 25

    root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    assert Solution().sumNumbers(root) == 1026