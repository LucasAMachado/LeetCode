# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Solution 1 -> Time Complexity : O(logn) : Space Complexity : O(1)
class Solution:
    def guessNumber(self, n: int) -> int:
        low: int = 1
        high: int = n

        while low <= high:
            m = (low + high) // 2

            if guess(m) > 0:
                # guess was to low
                low = m + 1
            elif guess(m) < 0:
                # guess was to high
                high = m - 1
            else:
                return m

        return -1
