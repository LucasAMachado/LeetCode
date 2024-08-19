from collections import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1 : Time Complexity : O(nlogn), Space Complexity : O(logn)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = self.getMidPoint(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def merge(self, list1, list2):

        dummy = ListNode()
        curr = dummy

        while list1 and list2:

            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2

        return dummy.next

    def getMidPoint(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Solution 2 : (Not Efficent), Time Complexity : O(nlogn), Space Complexity : O(n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a list with the nodes in that list (a list of nodes)
        # Then perform merge sort on that list of nodes to create the sorted list
        # Then turn the list into a linked list and return it

        # Check if it is an empty list
        if not head:
            return head

        un_sorted_list: list = []
        listNode: ListNode = head

        # Create a list of nodes
        while listNode:
            un_sorted_list.append(listNode.val)
            listNode = listNode.next

        sorted_list = self.mergeSort(
            un_sorted_list, 0, len(un_sorted_list) - 1)

        dummy = ListNode(0)
        cur = dummy
        for node in sorted_list:
            cur.next = node
            cur = cur.next

        return dummy.next

    # Merge sort on the list
    def mergeSort(self, arr: list, l: int, r: int) -> list:

        # Base case
        if (r - l + 1) <= 1:
            return arr

        # Get the mid point
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)

        self.merge(arr, l, m, r)

        return arr

    def merge(self, arr: list, l: int, m: int, r: int) -> list:

        # Create the left and right lists
        left: list = arr[l, m + 1]
        right: list = arr[m + 1, r + 1]

        # Pointers

        i: int = l
        j: int = 0
        k: int = 0

        while j < len(left) and k < len(right):

            if left[j].val < right[k].val:
                arr[i] = left[j]
                k += 1
            else:
                arr[i] = right[j]
                j += 1
            i += 1

        # Add the rest of the list
        while j < len(left):
            arr[i] = right[j]
            j += 1
            i += 1

        while k < len(right):
            arr[i] = right[k]
            k += 1
            i += 1

        return arr

