class Solution:
    """
    n = len(nums)
    k = k % n
    if k == 0: return
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    """
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        r = k % n
        if r == 0:
            return None
        revert_in_place(nums, 0, n - 1)
        revert_in_place(nums, 0, r - 1)
        revert_in_place(nums, r, n - 1)


def revert_in_place(nums, start, end):
    while start < end:
        tmp = nums[start]
        nums[start] = nums[end]
        nums[end] = tmp
        start += 1
        end -= 1
