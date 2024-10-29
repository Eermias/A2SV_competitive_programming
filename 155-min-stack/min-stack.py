class MinStack:

    def __init__(self):
        self.stack = [float('inf')]
        self.minimum = [float('inf')]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum.append(min(val, self.minimum[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()