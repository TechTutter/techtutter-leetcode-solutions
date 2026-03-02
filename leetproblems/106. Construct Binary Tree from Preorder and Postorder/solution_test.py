from solution import Solution, TreeNode

def traverse_inorder(node):
    if not node:
        return []
    return traverse_inorder(node.left) + [node.val] + traverse_inorder(node.right)

def traverse_postorder(node):
    if not node:
        return []
    return traverse_postorder(node.left) + traverse_postorder(node.right) + [node.val]

class TestSolution():
    def test_testcase1(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        s = Solution()
        n = s.buildTree(inorder, postorder)

        assert traverse_inorder(n) == inorder
        assert traverse_postorder(n) == postorder

    def test_testcase2(self):
        inorder = [-1]
        postorder = [-1]    
        s = Solution()
        n = s.buildTree(inorder, postorder)

        assert traverse_inorder(n) == inorder
        assert traverse_postorder(n) == postorder