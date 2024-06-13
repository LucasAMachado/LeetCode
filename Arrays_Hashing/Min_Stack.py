class MinStack:
    def __init__(self):
        self.arr = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.minStack.append(
            min(val, self.minStack[-1] if self.minStack else val))

    def pop(self) -> None:
        self.arr.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
