# Solution 1 -> Time Complexity : O(n2), Space Complexity : O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        s1_counter, s2_counter = [0] * 26, [0] * 26

        for i in range(n1):
            s1_counter[ord(s1[i]) - 97] += 1
            s2_counter[ord(s2[i]) - 97] += 1

        if s1_counter == s2_counter:
            return True

        for i in range(n1, n2):
            s2_counter[ord(s2[i]) - 97] += 1
            # Delete the value that we need to remove form the window
            s2_counter[ord(s2[i - n1]) - 97] -= 1
            if s1_counter == s2_counter:
                return True

        return False
