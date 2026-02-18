from solution import Solution, TreeNode


class TestExerciseName:
    def test_testcase1(self):
        n1 = TreeNode(5)
        n2 = TreeNode(4)
        n3 = TreeNode(8)
        n4 = TreeNode(11)
        n5 = TreeNode(13)
        n6 = TreeNode(4)
        n7 = TreeNode(7)
        n8 = TreeNode(2)
        n9 = TreeNode(1)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n4.left = n7
        n4.right = n8
        n3.left = n5
        n3.right = n6
        n6.right = n9
        assert Solution().hasPathSum(n1, 22) == True
        
