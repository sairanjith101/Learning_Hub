from collections import deque

# Initialize an empty queue
queue = deque()

# Enqueue operation
def enqueue(value):
    queue.append(value)
    print(f"Enqueued {value}")

# Dequeue operation
def dequeue():
    if queue:
        value = queue.popleft()
        print(f"Dequeued {value}")
        return value
    else:
        print("Queue is empty, cannot dequeue")
        return None

# Peek operation
def peek():
    if queue:
        print(f"Front of the queue: {queue[0]}")
        return queue[0]
    else:
        print("Queue is empty")
        return None

# Example usage
enqueue(1)
enqueue(2)
enqueue(3)
print("Queue:", list(queue))

dequeue()
peek()
print("Queue after dequeue:", list(queue))
