class Solution:
    def maxProfit(self, prices) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i]-buy > profit:
                profit = prices[i]-buy
        return profit


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
