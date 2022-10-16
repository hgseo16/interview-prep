class Solution(object):
    #     def maxProfit(self, prices):
    #         left, right = 0, 1 # index
    #         maxProfit = 0

    #         while right < len(prices):
    #             if prices[left] < prices[right]:
    #                 profit = prices[right] - prices[left]
    #                 maxProfit = max(maxProfit, profit)
    #             else:
    #                 left = right
    #             right += 1

    #         return maxProfit

    def maxProfit(self, prices):
        minValue = prices[0]
        maxProfit = 0

        for i, currPrice in enumerate(prices):
            if currPrice < minValue:
                minValue = currPrice
            elif currPrice - minValue > maxProfit:
                maxProfit = currPrice - minValue

        return maxProfit
