import pytest
from Reverse_Linked_List import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def main():
    test_1()
    test_2()
    test_3()


def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr


def test_1():
    sol = Solution()
    head = array_to_linked_list([1, 2, 3, 4, 5])
    reversed_head = sol.reverseList(head)
    assert linked_list_to_array(reversed_head) == [5, 4, 3, 2, 1]


def test_2():
    sol = Solution()
    head = array_to_linked_list([1, 2])
    reversed_head = sol.reverseList(head)
    assert linked_list_to_array(reversed_head) == [2, 1]


def test_3():
    sol = Solution()
    head = array_to_linked_list([1, 2, 6, 2, 6, 72,])
    reversed_head = sol.reverseList(head)
    assert linked_list_to_array(reversed_head) == [72, 6, 2, 6, 2, 1]


if __name__ == "__main__":
    main()
