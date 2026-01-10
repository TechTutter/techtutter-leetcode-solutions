class Solution:
    """
    length = len(nums)
    if length < 2: return nums[0]
    sorted_nums = sort(nums)
    return sorted_nums[length // 2]  # Majority element must be at the middle after sorting
    """
    def majorityElement(self, nums: list[int]) -> int:
        length = len(nums)
        if (length < 2):
            return nums[0]

        sorted_nums = sorted(nums)
        half = length//2
        return sorted_nums[half]
