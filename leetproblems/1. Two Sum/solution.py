class Solution:
    """
    for each number in nums:
        if number is in complementaries:
            return [complementaries[number], current_index]
        store complement (target - number) in complementaries -> current_index
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complementaries = {}

        for i, x in enumerate(nums):
            if x in complementaries:
                return [complementaries[x], i]

            complementaries[target - x] = i
