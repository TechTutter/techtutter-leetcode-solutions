from solution import Solution, TreeNode


def traverse_inorder(node):
    if node is None:
        return []
    return traverse_inorder(node.left) + [node.val] + traverse_inorder(node.right)


def traverse_preorder(node):
    if node is None:
        return []
    return [node.val] + traverse_preorder(node.left) + traverse_preorder(node.right)


class TestConvertSortedArrayToBinarySearchTree:
    def test_testcase1(self):
        s = Solution()
        root = s.sortedArrayToBST([-10, -3, 0, 5, 9])
        assert root.val == 0
        assert root.left.val == -10
        assert root.right.val == 5
        assert root.left.right.val == -3
        assert root.right.right.val == 9

    def test_testcase2(self):
        s = Solution()
        root = s.sortedArrayToBST([1, 3])
        assert root.val == 1
        assert root.right.val == 3
