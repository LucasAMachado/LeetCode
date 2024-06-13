from typing import List

# Solution One -> O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        found = set()

        for num in nums:
            if num not in found:
                found.add(num)
            elif num in found:
                return True

        return False

# Solution Two -> O(nlogn)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        sortedNums = sorted(nums) # Takes O(nlongn) to sort an array in python

        for i in range(1, len(sortedNums)):
            if sortedNums[i - 1] == sortedNums[i]:
                return True

        return False

def main():
    # Testing
    solution = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(solution.containsDuplicate(nums, 2))


if __name__ == "__main__":
    main()
