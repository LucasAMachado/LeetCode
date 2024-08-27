from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of cols

        l, r = 0, m * n - 1  # left and right pointer

        while l <= r:
            m = (l + r) // 2  # mid point
            row = m // n  # index divided by number of cols
            col = m % n  # index mod number of cols

            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True

        return False
