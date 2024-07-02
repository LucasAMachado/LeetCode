from typing import List

# Solution 1 -> Time complexity: O(4^n), Space complexity: O(4^n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(closedN, openN):
            if closedN == openN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(closedN, openN + 1)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(closedN + 1, openN)
                stack.pop()

        backtrack(0, 0)
        return res
