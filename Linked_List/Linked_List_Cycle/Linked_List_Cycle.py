from collections import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1 -> Time Complexity : O(n), Space Complexity O(n)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         hashset = set()

#         while head:
#             if head in hashset:
#                 return True
#             else:
#                 hashset.add(head)
#             head = head.next

#         return False

# Solution 2: Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using Floyd's Tortise and hare algo
        s, f = head, head  # s : slow , f : fast

        while f and f.next:
            s = s.next
            f = f.next.next

            if s == f:
                return True
        return False