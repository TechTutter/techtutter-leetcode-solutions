class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1

        while lo <= hi:
            mid_idx = (lo + hi) // 2

            left = nums[mid_idx - 1] if mid_idx - 1 >= 0 else -float('inf')
            right = nums[mid_idx + 1] if mid_idx + 1 < n else -float('inf')
            mid = nums[mid_idx]

            if mid > right and mid > left: return mid_idx 
            elif left > right: hi = mid_idx - 1
            else: lo = mid_idx + 1