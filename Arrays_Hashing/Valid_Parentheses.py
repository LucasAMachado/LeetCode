from typing import List

# Solution 1 -> O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep tracck of characters
        stack = []

        # Hash map to keep track of key value pairs
        map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # Check if the current "c" is a closing bracket
            if c in map:
               # Check to make sure the stack is not empty because we cannot
                # add a closing bracket to an empty stack
                # Also, check if the last element on the stack corresponds to the closing bracket
                if stack and stack[-1] == map[c]:
                    # Remove the open bracket form the stack
                    stack.pop()
                else:
                    return False
            else:
                # Add all open brackets to the stack
                stack.append(c)

        # Check to make sure that the stack is empty and return it
        return not stack
def main():
    # For testing testing
    solution = Solution()
    s = "()[]"
    print(solution.isValid(s))


if __name__ == "__main__":
    main()
