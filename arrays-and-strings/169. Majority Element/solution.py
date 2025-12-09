class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        length = len(nums)
        if (length < 2):
            return nums[0]

        sorted_nums = sorted(nums)
        half = length//2
        return sorted_nums[half]
