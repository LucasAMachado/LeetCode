from collections import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1 : Time Complexity O(nlogn), Space Complexity O(n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        arr = []

        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next

        arr.sort()

        dummy = ListNode(None)
        curr = dummy

        for val in arr:
            newNode = ListNode(val)
            curr.next = newNode
            curr = curr.next

        return dummy.next

# Solutoin 2 : Time Complexity : O(nlogk), Space Complexity : O(1)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            currentMerged = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                currentMerged.append(self.mergeLists(list1, list2))
            lists = currentMerged

        return lists[0]

    def mergeLists(self, list1, list2):
        dummy = ListNode(None)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next
