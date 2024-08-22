from typing import List

# Solution 1 : Time Complexity : O(n), Space Complexity : O(1       )
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []

        # create the bucket array with empty buckets
        counts : list = [0] * 3

        # add the values to there bucket in the bucket arr
        for num in nums:
            counts[num] += 1


        i : int = 0

        # take the values form the bucket and add them into the res list
        for index in range(len(counts)):
            for _ in range(counts[index]):
                nums[i] = index
                i += 1


