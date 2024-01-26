#121. Best Time to Buy and Sell Stock
from ast import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # left and right pointer
        l, r = 0, 0

        # default max profit
        maxProfit = 0

        while r < len(prices):
            # checking if the lowest current prices minus current max is greater than the current profit
            # if so then set the max profit to the new profit
            if prices[l] < prices[r]:
                tempProfit = prices[r] - prices[l]
                maxProfit = max(tempProfit, maxProfit)
            else:
                l = r
            r += 1

        return maxProfit
