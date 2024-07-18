from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solutoin 1 -> Time Complexity : O(n), Space Complexity : O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Split the lists into two halfs
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # Reverse the second half of the list   
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge the two lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            
