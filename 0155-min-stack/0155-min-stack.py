class MinStack:

    def __init__(self):
        self.base = 2**32
        self.m = self.base
        self.stack = []
        
    def push(self, val: int) -> None:
        if val < self.m:
            self.m = val
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop(-1)
        if len(self.stack)>0:
            self.m = min(self.stack)
        else:
            self.m = self.base
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()