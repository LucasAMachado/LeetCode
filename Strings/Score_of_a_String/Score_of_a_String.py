# Solution 1 -> O(n)
class Solution:
    def scoreOfString(self, s: str) -> int:
        i, j = 0, 1

        res = 0

        while i + 1 < len(s):
            res += abs(ord(s[i]) - ord(s[j]))
            i += 1
            j += 1

        return res

# Solution 2 -> O(n)
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1):
            res += abs(ord(s[i]) - ord(s[i+1]))

        return res
