class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        # implement this
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        # implement this
        if self.stack:
            item = self.stack.pop()
            if self.max_stack and item == self.max_stack[-1]:
                self.max_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_max(self):
        return self.max_stack[-1] if self.max_stack else None

# A few print statements to test the implementation
stack = MaxStack()
stack.push(5)
print(stack.get_max())  # Expected: 5
stack.push(1)
print(stack.get_max())  # Expected: 5
stack.push(6)
print(stack.get_max())  # Expected: 6
stack.pop()
print(stack.get_max())  # Expected: 5
