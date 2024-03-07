#1431. kids with the greatest number of candies


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []

        m = max(candies)  # Time complexity: O(n), where n is the number of kids

        for kid in candies:  # O(n) traversal over candies list
            result.append(kid + extraCandies >= m)

        return result

# Overall Time Complexity: O(n), Space Complexity: O(n) for the result list
