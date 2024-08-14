
# Solution 1 O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check if the lenghts are equal so that we can use one for loop
        if len(s) != len(t):
            return False

        # Set our counter maps
        s_counter, t_counter = {}, {}

        # Fill in our counter maps and keep track of the count of each char
        for i in range(len(s)):
            s_counter[s[i]] = 1 + s_counter.get(s[i], 0)
            t_counter[t[i]] = 1 + t_counter.get(t[i], 0)

        # Loop over one of the counters and make sure that the counts of each letter are the same
        for char in s_counter:
            if s_counter[char] != t_counter.get(char, 0):
                return False

        return True


# Solution 2 O(n)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_map = {}
#         t_map = {}

#         for char in s:
#             s_map[char] = 1 if char not in s_map else s_map[char] + 1

#         for char in t:
#             t_map[char] = 1 if char not in t_map else t_map[char] + 1

#         return s_map == t_map


# Solution 3 O(nlogn)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)


def main():
    # Testing
    solution = Solution()
    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))


if __name__ == "__main__":
    main()
