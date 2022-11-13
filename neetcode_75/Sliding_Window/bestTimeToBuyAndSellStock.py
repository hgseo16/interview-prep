class Solution:
    def maxProfit(self,prices):
        buy = 0
        sell = 0
        m = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                m = max(profit, m)
            else:
                buy = sell
            sell += 1
            
        return m
