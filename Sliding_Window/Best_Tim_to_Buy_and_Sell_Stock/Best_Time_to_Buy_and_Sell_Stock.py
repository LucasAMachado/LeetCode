from typing import List


# Solution 1 -> Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left -> buy
        # right -> sell
        l : int = 0
        r : int = 1
        maxP : int = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, (prices[r] - prices[l]))
            else :
                # This means that we have found a new 
                # min price thus we was to buy at that 
                # low price rather than a higher price
                l = r

            r += 1
        return maxP
            