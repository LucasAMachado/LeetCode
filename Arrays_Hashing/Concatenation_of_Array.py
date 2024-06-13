from typing import List


# Solution One -> O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Get the lenght of the nums list
        # create a new list that has double the size
        # iterate over the new list and add the values form the old list
        ans = [0] * len(nums) * 2
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]

        return ans

# Solution Two -> O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        # Repeat 2 times as we want to contact two lists
        for _ in range(2):
            for n in nums:
                ans.append(n)

        return ans

# For testing
def main():
    solution = Solution()
    nums = [1, 3, 2, 1]
    print(solution.getConcatenation(nums))


if __name__ == "__main__":
    main()
