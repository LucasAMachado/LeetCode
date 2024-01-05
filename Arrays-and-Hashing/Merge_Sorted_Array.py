from ast import List


# Solution Number 1 Using Three Pointers
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Last pointer
        last = m + n - 1

        # Running while there are elements in both arrays
        while m > 0 and n > 0:
            # If the last real element in nums1 greater then the last element in nums2
            # Set the last element in nums1 equal to the last real elment in nums 2
            # Move the pointer to the left in nums1
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                # Same idea but opposite as in the fist check
                nums1[last] = nums2[n-1]
                n -= 1
            # Shift the last pointer to the left
            last -= 1

        # If nums1 lenght = 0 but we still have elements in nums2 add then to the nums1
        while n > 0:
            nums1[last] = nums2[n-1]
            last -= 1
            n -= 1
