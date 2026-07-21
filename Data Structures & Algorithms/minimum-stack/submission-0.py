class MinStack:
    def __init__(self):
            self.stack = []
            self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)
        self.stack.append(val)
        return

    def pop(self) -> None:
        if not self.stack:
            return "underflow"
        x = self.stack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()
        return

    def top(self) -> int:
        if not self.stack:
            return "underflow"
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
