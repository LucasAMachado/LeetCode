from collections import defaultdict
from typing import List


# Solution 1 -> O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in nums:
            # Check if the num is the start of a sequence
            if (num - 1) not in numsSet:
                result = 0
                # Count the length of the current sequence by
                # checking how many number come after that are
                # one greater than the current num are in the numsSet
                while (num + result) in numsSet:
                    result += 1

                longest = max(longest, result)

        return longest


def main():
    # Testing
    solution = Solution()
    nums = [1, 2, 0, 1]
    print(solution.longestConsecutive(nums))


if __name__ == "__main__":
    main()
