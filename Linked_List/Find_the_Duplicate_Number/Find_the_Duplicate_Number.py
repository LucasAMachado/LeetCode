from typing import List

# Solution 1 : Brute Force, Time Complexity : O(n), Space Complexity : O(n) (Not allowed)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # Brute force using two loops

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return nums[i]
                
# Solution 2 : Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
