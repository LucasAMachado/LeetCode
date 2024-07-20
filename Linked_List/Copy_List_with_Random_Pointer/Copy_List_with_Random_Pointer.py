from collections import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Solution 1 : Time Complexity : O(n) Memory Complexity : O(n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapOldNew = {None, None} # {oldNode : newNode}

        cur = head
        while cur:
            copy = Node(cur.val)
            mapOldNew[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = mapOldNew[cur]
            copy.next = mapOldNew[cur.next]
            copy.random = mapOldNew[cur.random]
            cur = cur.next
        
        return mapOldNew[head]