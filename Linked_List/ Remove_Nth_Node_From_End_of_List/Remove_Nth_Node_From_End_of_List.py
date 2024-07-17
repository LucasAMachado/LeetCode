from collections import Optional
# # Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1 -> Time Complexity O(n) : Space Complexity : O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        left, right = dummy, head  # Left and right pointers

        # Shift the right pointer n nodes to the right
        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        # Delete the n'th node
        left.next = left.next.next

        return dummy.next
