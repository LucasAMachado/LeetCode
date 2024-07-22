from collections import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1 (Not very efficient, first solution that came to mind)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        chunk = []
        cur = head
        i = 0

        while cur:
            if i % k == 0:
                chunk.append([])

            chunk[-1].append(cur)
            cur = cur.next
            i += 1

        dummy = ListNode(None)
        res = dummy

        for group in chunk:
            if len(group) == k:
                group.reverse()

            for node in group:
                res.next = node
                res = res.next
        res.next = None

        return dummy.next
