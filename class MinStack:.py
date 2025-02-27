class MinStack:
    stack = []
    minval = 0
    def __init__(self):
    def push(self, val: int) -> None:
        stack.append(val)
        if val < minval:
            minval = val
    def pop(self) -> None:
        stack[-1] = None
    def top(self) -> int:
        return stack[-1]
    def getMin(self) -> int:
        return minval