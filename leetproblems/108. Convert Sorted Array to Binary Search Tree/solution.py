class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        def recursive_tree_builder(start: int, end: int) -> None:
            if end < start:
                return None

            mid = (end + start) // 2
            x = TreeNode(nums[mid])
            x.left = recursive_tree_builder(start, mid - 1)
            x.right = recursive_tree_builder(mid + 1, end)
            return x

        return recursive_tree_builder(0, len(nums) - 1)
