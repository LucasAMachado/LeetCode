# Solution 1 : Time Complexity : O(2^n), Space Complexity :  O(n) (was not accepted by leetcode)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStaris(n-1) + self.climbStairs(n-2)

# Soluton 2 : Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
