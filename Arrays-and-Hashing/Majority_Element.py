# 169. Majority Element
from ast import List

#Solution Number 1 [HashMap]
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        return max(hashMap, key=hashMap.get)
