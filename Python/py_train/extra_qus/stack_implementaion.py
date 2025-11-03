from queue import LifoQueue

# Initialize a stack using LifoQueue
stack = LifoQueue()

# Push operation
stack.put('a')
stack.put('b')
stack.put('c')

# Peek operation (get top element without removing)
if not stack.empty():
    top = stack.get()
    print("Top of stack:", top)
    stack.put(top)  # Add the element back to the stack
else:
    print("Stack is empty")

# Pop operations
print("Stack before pops:")
while not stack.empty():
    print("Popped:", stack.get())

# Check if stack is empty
print("Stack Empty:", stack.empty())

# Check if stack is full
# (optional, only if you've set a max size for the stack)
print("Stack Full:", stack.full())
print("Current size of stack:", stack.qsize())
