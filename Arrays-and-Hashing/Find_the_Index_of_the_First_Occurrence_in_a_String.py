# 28. Find the Index of the First Occurrence in a String

class Solution:
    # Solution Brute Force Using While Loop
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i:i+len(needle)] == needle:
                return i
            i += 1

        return -1
    # Solution Brute Force Using For Loop

    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
