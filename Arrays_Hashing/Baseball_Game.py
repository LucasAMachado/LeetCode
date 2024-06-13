from typing import List

# Solution 1 -> O(n)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Plan
        # 1 Create a record list (to hold the records)
        # 2 Iterate through the operations list appending the operation to the record_list if it
        # a number
        # 3 If it is an operation perform the operation on the record_list
        # 4 return the sum of the record list using sum(record_list)
        stack = []

        for operation in operations:
            if operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "+":
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(operation))

        return sum(stack)


# For testing
def main():
    solution = Solution()
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(solution.calPoints(ops))


if __name__ == "__main__":
    main()
