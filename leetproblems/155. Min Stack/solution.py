class MinStack:
    def __init__(self):
        self.values = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.values.append(val)

        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.values.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        