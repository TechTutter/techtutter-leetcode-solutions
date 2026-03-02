from solution import Solution, TreeNode

def traverse_inorder(node):
    if not node:
        return []
    return traverse_inorder(node.left) + [node.val] + traverse_inorder(node.right)

def traverse_preorder(node):
    if not node:
        return []
    return [node.val] + traverse_preorder(node.left) + traverse_preorder(node.right)

class TestSolution():
    def test_testcase1():
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        s = Solution()
        n = s.buildTree(preorder, inorder)

        assert(traverse_inorder(n) == inorder)
        assert(traverse_preorder(n) == preorder)

    def test_testcase2():
        preorder = [-1]
        inorder = [-1]
        s = Solution()
        n = s.buildTree(preorder, inorder)

        assert(traverse_inorder(n) == inorder)
        assert(traverse_preorder(n) == preorder)