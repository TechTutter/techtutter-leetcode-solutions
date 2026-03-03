class Solution:
    def __init__(self):
        self.max_profit_until_i = {}

    def rob(self, nums: list[int]) -> int:
        return self.dynamic_robbing(nums, len(nums) - 1)

    def dynamic_robbing(self, nums: list[int], n):
        if n in self.max_profit_until_i:
            return self.max_profit_until_i[n]

        if n < 0:
            return 0
        if n < 2:
            self.max_profit_until_i[n] =  max(nums[n], self.dynamic_robbing(nums, n - 1))
            return self.max_profit_until_i[n]
        else:
            self.max_profit_until_i[n] = max(nums[n] + self.dynamic_robbing(nums, n - 2), self.dynamic_robbing(nums, n - 1))
            print(n, self.max_profit_until_i[n])

        return self.max_profit_until_i[n]
        