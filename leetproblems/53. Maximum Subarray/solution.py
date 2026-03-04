class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        dp = [0] * n 
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = nums[i] + max(0, dp[i-1])
        return max(dp)