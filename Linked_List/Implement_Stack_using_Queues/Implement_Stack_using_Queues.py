from collections import deque

# Solution 1 -> Time Complexity O(n)
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # Iterate until the end of the que
        for i in range(len(self.q) - 1):
            # Pop the left most element and then append it
            # to the end of the que
            self.q.append(self.q.popleft())

        # pop the left element now and return it
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0

# (Not what supposed to use a linked list but I have done it for practice), Solution 2 -> Time Complexity : O(n) for all operations, Space Complexity : O(n)
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None


class MyQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x: int) -> None:
        newNode = ListNode(x)

        if self.empty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return None

        headvValue = self.head.value

        self.head = self.head.next
        self.size -= 1

        return headvValue

    def peek(self) -> int:
        if self.empty():
            return None

        return self.head.value

    def empty(self) -> bool:
        return self.size == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# # param_3 = obj.top()
# param_4 = obj.empty()
