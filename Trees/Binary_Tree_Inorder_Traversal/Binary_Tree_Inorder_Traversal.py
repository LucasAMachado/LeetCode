from collections import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solutoin 1 - Time Complexity : O(N), Space Complexity : O(N) (Recurive)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inner(root):
            if not root:
                return

            inner(root.left)
            res.append(root.val)
            inner(root.right)

        inner(root)
        return res

# Solutoin 1 - Time Complexity : O(N), Space Complexity : O(N) (Iterative)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res
