# 27 Remove Element
from ast import List

# Solution Number 1 Using Two Pointers (Fast but not very memory efficient)
def removeElement(self, nums: List[int], val: int) -> int:
    i, j = 0, 0

    while j < len(nums):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
            j += 1
    return i

# Solution Number 2 Memory Efficient
def removeElement(self, nums: List[int], val: int) -> int:
    i = 0

    while i < len(nums):
        #If value found then remove it 
        if nums[i] == val:
            nums.pop(i)
        #Otherwise keep it and go to the next
        else:
            i += 1
    #The length of all of the non val items
    return len(nums)