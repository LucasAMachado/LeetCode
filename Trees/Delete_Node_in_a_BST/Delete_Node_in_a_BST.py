from collections import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time Complexity : O(logn), Space Complexity : O(logn)
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minKeyNode = self.minValueNode(root.right)
                root.val = minKeyNode.val
                root.right = self.deleteNode(root.right, minKeyNode.val)

        return root

    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left

        return curr
