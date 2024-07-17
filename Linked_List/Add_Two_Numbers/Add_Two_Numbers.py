from collections import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1 -> Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            value = val1 + val2 + carry
            # Get the carry value
            carry = value // 10
            # Make sure that we are working with one digit
            value = value % 10
            cur.next = ListNode(value)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
# Solution 2 Brute Force (Not a good solution)
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         sum1, sum2, newSum = 0, 0, 0
#         dummy = ListNode(0)
#         res = dummy
#         multiplier = 1

#         while l1:
#             sum1 += (l1.val * multiplier)
#             multiplier *= 10
#             l1 = l1.next

#         multiplier = 1
#         while l2:
#             sum2 += (l2.val * multiplier)
#             multiplier *= 10
#             l2 = l2.next

#         newSum = str(sum1 + sum2)[::-1]

#         for i in range(len(newSum)):
#             res.next = ListNode(int(newSum[i]))
#             res = res.next

        # return dummy.next
