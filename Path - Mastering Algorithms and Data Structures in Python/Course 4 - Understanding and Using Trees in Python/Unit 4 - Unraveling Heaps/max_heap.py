# Import necessary libraries
import heapq

# Create an empty MaxHeap
maxHeap = []

# A function to insert nodes into the MaxHeap while maintaining the heap property
def insert(nodes):
    for node in nodes:
        heapq.heappush(maxHeap, -node)
    print(f"Max Heap after insertion: {maxHeap}")

# A function to delete the largest node from the MaxHeap
def delete():
    largest = -heapq.heappop(maxHeap)
    print(f"Max Heap after deletion of largest node: {maxHeap}")

# Spaceships identified by the last 2 digits of their license numbers
spaceships = [28, 14, 35, 55, 68, 72, 47, 19, 11, 32]

insert(spaceships)  # Add all spacecrafts to the queue

delete() # Delete the spacecraft with the largest license number
