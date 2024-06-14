from collections import defaultdict
from typing import List


# Solution 1 -> O(nlogn)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         wordMap = {}  # sortedWord: word

#         for word in strs:
#             sortedWord = ''.join(sorted(word))  # Sort the current word

#             # If the sorted word is in the wordMap then we add the word to the current list containing anagrams
#             if sortedWord in wordMap:
#                 wordMap[sortedWord].append(word)

#             # Add the word in a list to the wordMap (meaning we do not have an anagram match for this word)
#             else:
#                 wordMap[sortedWord] = [word]

#         return list(wordMap.values())


# Solution 2 -> O(m * n)
# Where m -> number of words in the lsit
#       n -> average length of each word in the list
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # number of characters in the alphabet

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()


def main():
    # Testing
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))


if __name__ == "__main__":
    main()
