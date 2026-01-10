class Solution:
    """
    left = 0, current_sum = 0, min_length = infinity
    for right from 0 to n-1:
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left++
    return 0 if min_length is infinity else min_length
    """
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        curr_sum = 0
        window = float('inf')

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum >= target:
                window = min(window, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if window == float('inf') else window