import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        left = 0, window = 0, total = 0
        for i in range(len(nums)):
            total += current value
            while target is reached:
                store current window size, if lower than current
                subtract left from total
                increase left
        """
        if target == 0: return 0
        
        left = total = 0
        window = math.inf

        for right, x in enumerate(nums):
            total += x
            while total >= target:
                window = min(window, right - left + 1)
                total -= nums[left]
                left += 1
        
        return window if window != math.inf else 0