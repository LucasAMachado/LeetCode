from typing import List

# Solution 1 -> O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# Solution 2 -> O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in nums_map:
                return [nums_map[complement], i]
            
            nums_map[nums[i]] = i

# Solution 3 -> O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in nums_map:
                return [nums_map[diff], index]
            
            nums_map[num] = index

def main():
    # Testing
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))


if __name__ == "__main__":
    main()
