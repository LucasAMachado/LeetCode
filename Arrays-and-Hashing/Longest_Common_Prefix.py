# 14. Longest Common Prefix

# Solution Using Two Pointers
from ast import List


class Solution:
    # Solution Number 1 Using strip()
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        temp = s.strip()
        for i in range(len(temp)-1, -1, -1):
            if temp[i] != " ":
                word += temp[i]
            else:
                break
        return len(word)

    # Solution Number 1 Not Using s.strip()
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        while s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
