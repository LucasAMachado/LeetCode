# 1768. Merge Strings Alternately
# Solution Number 1 Brute Force
def mergeAlternately(word1: str, word2: str) -> str:

    merged = ''
    minStr = min(len(word1), len(word2))
    i = 0

    while i < minStr:
        merged += word1[i]
        merged += word2[i]

        i += 1

    merged += word1[i:]
    merged += word2[i:]

    return merged

# Solution Number Two Pointers
def mergeAlternately(word1: str, word2: str) -> str:
    i, j = 0, 0
    result = []

    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    result.append(word1[i:])
    result.append(word2[j:])

    return "".join(result)
