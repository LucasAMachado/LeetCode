from typing import List

# Solution 1 => Time Complexity : O(n) Memory Complexity : O(n) (Not a good solution)
class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = []
        maxRight = []
        res = 0

        for i in range(len(height)):
            if i == 0:
                maxLeft.append(0)
            else:
                maxLeft.append(max(height[:i]))

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                maxRight.append(0)
            else:
                maxRight.append(max(height[i+1:]))

        maxRight.reverse()

        for i in range(len(maxLeft)):
            temp = min(maxLeft[i], maxRight[i]) - height[i]

            if temp >= 0:
                res += temp

        return res


# Solution 2 => Time Complexity : O(n) Memory Complexity : O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                r -= 1

        return res