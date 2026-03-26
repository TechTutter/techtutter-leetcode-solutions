class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        # Find the most profit I can make between prices[0:i] for each i < n
        lowest_entry_point = prices[0]
        local_best = 0
        best_profit_until_i = [0] * n

        for i in range(1, n):
            lowest_entry_point = min(lowest_entry_point, prices[i])
            local_best = max(local_best, prices[i] - lowest_entry_point)
            best_profit_until_i[i] = local_best

        # Find the best profit I can make within prices[i:n-1] for each i < n
        highest_selling_point = prices[n - 1]
        local_best = 0
        best_profit_from_i = [0] * n

        for i in range(n-2, -1, -1):
            highest_selling_point = max(highest_selling_point, prices[i])
            local_best = max(local_best, highest_selling_point - prices[i])
            best_profit_from_i[i] = local_best

        res = 0
        for i in range(n):
            sanitized_best_from_i = best_profit_from_i[i + 1] if i < n-1 else 0
            res = max(res, best_profit_until_i[i] + sanitized_best_from_i)

        return res