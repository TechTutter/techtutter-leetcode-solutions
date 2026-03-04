class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_gain = 0
        for i in range(1, n):
            gain = prices[i] - prices[i-1]
            max_gain = max(0, gain) + max_gain
        return max_gain
        

    def maxProfit_naive(self, prices: list[int]) -> int:
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