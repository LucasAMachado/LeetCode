from typing import List

# Solution 1 : Time Complexity : O(nlogn), Space Complexity : O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # merge sort helper (take in a l and r pointer)
        # base case
        # call merge sort helper on the left and the right lists
        # merge the lists
        # return the lists

        # merge helper
        # use three pointers
        # take in a middle point and a left and right pointer
        # merget the lists in sorted order
        # return the sorted list

        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, arr: list, l: int, r: int) -> list:

        # base case (only one el in the list)
        if (r - l) + 1 <= 1:
            return arr

        # Get the mid point (round down)
        m = (l + r) // 2

        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)

        # merge the lists
        self.merge(arr, l, m, r)

        return arr

    def merge(self, arr: list,  l: int, m: int, r: int) -> list:
        left: list = arr[l:m+1]
        right: list = arr[m+1:r+1]

        i: int = l
        j: int = 0  # for left list
        k: int = 0  # for right list

        while j < len(left) and k < len(right):

            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1

            i += 1

        while j < len(left):
            arr[i] = left[j]
            j += 1
            i += 1

        while k < len(right):
            arr[i] = right[k]
            k += 1
            i += 1

        return arr
