from typing import List
from typing import Counter
# Solutoin 1 -> Time Complexity : O(n) : Space Complexity : O(n)
# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         res = len(students)

#         counter = {}  # hash map : sandwiche : count

#         # Fill in our hash map with the sandwiche and the
#         # Count of the number of students who want each time of Sandwhich
#         for student in students:
#             if student not in counter:
#                 counter[student] = 1
#             else:
#                 counter[student] += 1

#         for sandwiche in sandwiches:
#             if sandwiche in counter and counter[sandwiche] > 0:
#                 res -= 1
#                 counter[sandwiche] -= 1
#             else:
#                 # No sandwiche that the students want
#                 return res

#         return res


# Solution 2 -> Time Complexity : O(n) : Space Complextiy : O(n)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        ctr = Counter(students)

        for s in sandwiches:
            if ctr[s] > 0:
                res -= 1
                ctr[s] -= 1
            else:
                return res

        return res
