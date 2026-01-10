class Solution:
    """
    min_price = infinity
    max_profit = 0
    for each price in prices:
        if price < min_price:
            min_price = price
        else if price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
    """
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