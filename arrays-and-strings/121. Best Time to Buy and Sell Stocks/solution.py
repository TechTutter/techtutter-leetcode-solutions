class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if(len(prices) < 2):
            return 0

        profit = 0
        maxProfit = 0
        minPrice = 10e6

        for p in prices:
            if(p < minPrice):
                minPrice = p

            profit = p - minPrice

            if(profit > maxProfit):
                maxProfit = profit

        return maxProfit