from typing import List

# Solution 1 -> Time Complexity : O(n * n!), Space Complexity : O(n * n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 0:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)

            # Add the value back that we removed
            nums.append(n)

        return res
