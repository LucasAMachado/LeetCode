from typing import List

# Solution One
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0  # Set our first pointer to 1

        # Set our second pointer to always be one index or more ahead of our j pointer
        for i in range(1, len(nums)):
            # Check if the num is not a duplicate and increment j
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        # Add one to j to ensure we get the correct count of unique elements
        return j + 1

# Solution Two - (very similar to solution One)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1  # Set our left pointer to be 1

        for r in range(1, len(nums)):
            # Check if the element in unique if so modify our list
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                # Increment our left pointer
                l += 1
        return l


def main():
    # Testing
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates(nums))


if __name__ == "__main__":
    main()
