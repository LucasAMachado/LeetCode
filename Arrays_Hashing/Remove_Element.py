from typing import List

# Solution One
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0  # Set our left pointer

        # Loop through nums with our right pointer
        for r in range(len(nums)):
            # Checking if the current num is not equal to our val,
            # if so then we set the value at our left pointer to that value
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1

        return l


def main():
    # Testing 
    solution = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(solution.removeElement(nums, 2))


if __name__ == "__main__":
    main()
