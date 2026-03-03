class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        STATE = state[i] is max strictly increasing subsequence up until i, included
        BASE = base is state[0] = 0
        TRANSITION = state[i] is 1 + max between all values in state[0:i] if nums[x] < nums[i]
        Build state bottom-up
        """
        n = len(nums)
        state = [1] * n

        for i in range(1, n):
            for x in range(i):
                if nums[x] < nums[i]:
                    state[i] = max(state[i], 1 + state[x])

        return max(state)
