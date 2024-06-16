from collections import defaultdict
from typing import List

# Solution 1 -> O(n^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)  # key : row, val : set
        colMap = defaultdict(set)  # key : row, val : set
        subMap = defaultdict(set)  # key : (r//3, c//3), val : set

        for r in range(9):
            for c in range(9):

                # Do not check the tile if it is equal to a .
                if board[r][c] == ".":
                    continue

                # Validate that the num has not appeard more than once in the rows, cols, and sub grids
                if (board[r][c] in rowMap[r]) or (board[r][c] in colMap[c]) or (board[r][c] in subMap[(r//3, c//3)]):
                    return False

                # Add all of the current numbers to the rows, cols, and subgrids
                rowMap[r].add(board[r][c])
                colMap[c].add(board[r][c])
                subMap[(r//3, c//3)].add(board[r][c])

        return True
