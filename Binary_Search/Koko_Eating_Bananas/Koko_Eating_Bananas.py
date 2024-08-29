from typing import List

# Solution 1 -> Time Complexity : O(n * log(max(piles))), Space Complexity : O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            time_taken = 0
            for pile in piles:
                time_taken += (pile + k - 1) // k

            if time_taken <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
