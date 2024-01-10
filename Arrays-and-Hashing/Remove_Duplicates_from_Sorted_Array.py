from ast import List

#Solution Number 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = set()
        i = 0
        while i < len(nums):
            if nums[i] in found:
               nums.pop(i)
            else:
                found.add(nums[i])
                i += 1

        return i
