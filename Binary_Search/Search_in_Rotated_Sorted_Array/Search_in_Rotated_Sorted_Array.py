from typing import List

# Solution 1 -> Time Complexity : O(logn), Space Complexity : O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1

        while l <= r:
            mid: int = (l + r) // 2

            if nums[mid] == target:
                return mid
            # Everything to the right is sorted
            if nums[mid] < nums[r]:
                # Chec if target falls in sorted range
                if nums[mid + 1] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Everything to the left is sorted
            else:
                # Check if target falls in sorted range
                if nums[l] <= target <= nums[mid - 1]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
