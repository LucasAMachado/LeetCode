from typing import List


# Solution 1 -> Time Complexity : O(n), Space Complexity : O(1)
# This is pretty good becuase we can get the sum from 0 to n using n(n+1)/2
# rather than having to use a for loop to get the sum from 1 to n
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        t_sum = (len(nums) * (len(nums) + 1)) // 2

        for num in nums:
            t_sum -= num

        return t_sum

# Solution 2 -> Time Complexity : O(n), Space Complexity : O(1)


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target_sum, real_sum = 0, 0

        for i in range(len(nums)):
            target_sum += (i + 1)

        for num in nums:
            real_sum += num

        return (target_sum - real_sum)


# Solution 3 -> Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res
