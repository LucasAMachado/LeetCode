from collections import defaultdict
from typing import List

# Solution 1 -> O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}  # num : occurrences

        # Set the count of each num in the num map
        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1

        # Get the key of the sorted dict for the first k elements
        topK = [item[0] for item in sorted(
            numsMap.items(), key=lambda item: item[1], reverse=True)[:k]]

        return topK  # [list of the nums]
    

# Solution 2 -> O(n) (Bucket Sort idea)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # num : count

        # Each index hold a list of nums with a freq of that index
        freq = [[] for i in range(len(nums) + 1)]

        # Count the number of times each number occurs
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # insert the nums with the freq of n in the freq arr
        for n, c in count.items():
            freq[c].append(n)

        res = []

        # Loop from right -> left in the freq arr and add the nums in each index to the res
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


def main():
    # Testing
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution.topKFrequent(nums, k))


if __name__ == "__main__":
    main()
