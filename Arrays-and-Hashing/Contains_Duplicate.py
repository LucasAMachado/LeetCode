from ast import List

# Solution Number 1
# If the number is in the set then it is a dupe


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


# Solution Number 2
# If the lenght of the set does not equal the length of the nums arr then there must be dups
    # Since a set cannot have dups
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (len(set(nums)) == len(nums))
