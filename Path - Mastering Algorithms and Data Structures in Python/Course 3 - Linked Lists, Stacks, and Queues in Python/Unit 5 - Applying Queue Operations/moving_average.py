from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.queue = deque()
        self.size = size
        self.total = 0

    def calculate_moving_average(self, word):
        # implement this
        if len(self.queue) == self.size:
            self.total -= len(self.queue.popleft())
        self.queue.append(word)
        self.total += len(word)
        return round(self.total / len(self.queue), 2)


# Test samples
ma = MovingAverage(3)
print(ma.calculate_moving_average('one'))  # Expected: 3.0
print(ma.calculate_moving_average('two'))  # Expected: 3.0
print(ma.calculate_moving_average('three'))  # Expected: 3.67
print(ma.calculate_moving_average('four'))  # Expected: 4.0
print(ma.calculate_moving_average('five'))  # Expected: 4.33
print(ma.calculate_moving_average('six'))  # Expected: 3.67
