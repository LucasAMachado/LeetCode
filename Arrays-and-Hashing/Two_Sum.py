from ast import List


# Solution Number 1 Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Solution Number 2


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums[i+1:]:
                return [i, nums.index(complement)]

# Solution Number 3 Hash Table


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashMap:
                return [hashMap[comp], i]
            hashMap[nums[i]] = i

        return []
