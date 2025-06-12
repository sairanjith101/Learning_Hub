class Stack:
    def __init__(self):
        self.container = []

    def push(self, val):
        self.container.append(val)

    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        else:
            return None  # or raise error

    def top(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return None

    def is_empty(self):
        return len(self.container) == 0


# Usage example:
stack = Stack()
stack.push(10)
stack.push(20)
print("Top:", stack.top())        # Output: 20
print("Popped:", stack.pop())     # Output: 20
print("Is empty?", stack.is_empty())  # Output: False
