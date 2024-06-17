# Solution 1 -> Time Complexity: O(n), Mem Complexity: O(1)
class Solution:
    def alphaNum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1

            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

# Solution 2 -> O(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         resized = [char.lower() for char in s if char.isalnum()]

#         return resized == resized[::-1]


# Solution 3 -> O(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:

#         resized = [char.lower() for char in s if char.isalnum()]

#         l, r = 0, len(resized) - 1

#         while l < ((len(resized)) / 2):
#             if resized[l] != resized[r]:
#                 return False

#             l += 1
#             r -= 1

#         return True
