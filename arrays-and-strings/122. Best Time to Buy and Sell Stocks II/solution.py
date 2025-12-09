class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if(len(prices) < 2):
            return 0

        profit = 0
        best_buy = best_sell = prices[0]

        for p in prices:
            if (p < best_buy):
                best_buy = p
                best_sell = p
            elif(p > best_sell):
                profit += p - best_buy
                best_buy = p
                best_sell = 0
        return profit