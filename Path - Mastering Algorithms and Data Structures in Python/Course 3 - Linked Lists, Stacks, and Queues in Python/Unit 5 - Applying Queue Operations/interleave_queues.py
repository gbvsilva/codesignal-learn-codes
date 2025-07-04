from collections import deque

def interleave_queues(queue1, queue2):
    # implement this
    interleave_queue = deque(queue1 + queue2)
    half_size = len(interleave_queue) // 2
    first_half = deque()

    for _ in range(half_size):
        first_half.append(interleave_queue.popleft())

    while first_half:
        interleave_queue.append(first_half.popleft())
        if interleave_queue:
            interleave_queue.append(interleave_queue.popleft())

    return list(interleave_queue)

# Test cases
print(interleave_queues(deque([1, 2, 3, 4, 5]), deque([6, 7, 8, 9, 10])))
# Expected output: [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
print(interleave_queues(deque([1]), deque([2])))
# Expected output: [1, 2]
print(interleave_queues(deque([1, 3, 5]), deque([2, 4, 6])))
# Expected output: [1, 2, 3, 4, 5, 6]
