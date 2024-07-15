# Solution 1 : Time Complexity O(n) , Space Complexity O(n)
class ListNode:
    def __init__(self, homepage: str):
        self.url = homepage
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.cur.next = newNode
        newNode.prev = self.cur
        self.cur = newNode

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
