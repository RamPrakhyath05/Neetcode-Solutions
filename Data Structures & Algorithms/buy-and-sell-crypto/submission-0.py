class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProfit = 0
        profit = 0
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell 
            else:
                profit = prices[sell] - prices[buy]
                maxProfit = max(profit, maxProfit)
            sell += 1
        return maxProfit