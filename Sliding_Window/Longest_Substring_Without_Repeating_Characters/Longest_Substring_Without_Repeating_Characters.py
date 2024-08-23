# Solution 1 : Time Complexity : O(n), Space Complexity : O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        wSet = set()
        l, r, res = 0, 0, 0

        while r < len(s):
            if s[r] not in wSet:
                wSet.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                wSet.remove(s[l])
                l += 1

        return res
