from typing import List

# Solution 1 -> Time Complexity : O(nlogn) Space Complexity : O(n)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = [[p, s] for p, s in zip(position, speed)]

        res = []  # Keep track of the car fleets

        # Loop through the positions right -> left
        for p, s in sorted(positions)[::-1]:
            res.append((target - p) / s)
            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()

        return len(res)
