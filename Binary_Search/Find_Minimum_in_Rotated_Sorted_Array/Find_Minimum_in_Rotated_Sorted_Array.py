from typing import List

# Solution 1: Time Complexity : O(logn) Space Complexity : O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res: int = nums[0]

        l: int = 0
        r: int = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:  # sub array is sorted
                return min(res, nums[l])

            m: int = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:  # search the right sub array
                l = m + 1
            else:
                r = m - 1  # search the left sub array

        return res
