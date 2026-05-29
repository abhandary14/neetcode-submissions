class MinStack:

    def __init__(self):
        self.stack = []
        self.minim = float('inf')

    def push(self, val: int) -> None: # keep track of current minimum at each push
        if not self.stack:
            self.minim = val
        else:
            self.minim = min(self.minim, val)
        self.stack.append((val, self.minim))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minim = self.stack[-1][1]
        else:
            self.minim = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minim
