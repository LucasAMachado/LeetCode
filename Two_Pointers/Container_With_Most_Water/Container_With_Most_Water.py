from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


def main():
    sol = Solution()
    height = [5, 4, 3, 2, 1]
    print(sol.maxArea(height))


main()
