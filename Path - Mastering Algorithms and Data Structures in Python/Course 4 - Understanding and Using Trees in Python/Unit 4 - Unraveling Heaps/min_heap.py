import heapq

# Create an empty MinHeap
minHeap = []

def insert(random_numbers):
    for number in random_numbers:
        # TODO: insert number to minHeap
        heapq.heappush(minHeap, number)
    print(f"Min Heap after inserting random numbers: {minHeap}")

def delete():
    # TODO: Delete the smallest node from the minHeap
    try:
        smallest = heapq.heappop(minHeap)
        return smallest
    except:
        return None

# Random numbers generated by a hypothetic radar for a real-world simulation
randomNumbers = [23, 42, 14, 30, 27, 56, 14, 9, 5, 21, 34]

# Inserting the generated random numbers into the MinHeap
insert(randomNumbers)

# Removing the smallest numbers from the MinHeap for a real-world simulation
for i in range(15):
    minNumber = delete()
    if minNumber is None:
      print("Min Heap is empty. No numbers to delete.")
    else:
      print(f"Min Heap after removing the smallest number {minNumber}: {minHeap}")
