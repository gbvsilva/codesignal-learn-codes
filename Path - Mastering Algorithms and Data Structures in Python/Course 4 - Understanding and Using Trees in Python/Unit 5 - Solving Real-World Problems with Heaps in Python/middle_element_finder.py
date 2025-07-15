import heapq

class MiddleElementFinder:
    def __init__(self):
        self.heaps = [], []
        self.arr = []

    def add_num(self, num: int) -> None:
        # implement this
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))
        self.arr.append(num)

    def middle_element(self) -> int:
        # implement this
        small, large = self.heaps
        if len(large) > len(small):
            return int(float(large[0]))
        return int(float((large[0] - small[0]) / 2.0))

    def naive_middle_element(self) -> int:
        # This is a naive implementation that sorts the array to find the middle element
        if not self.arr:
            return 0
        sorted_arr = sorted(self.arr)
        mid_index = len(sorted_arr) // 2
        return sorted_arr[mid_index] if len(sorted_arr) % 2 != 0 else (sorted_arr[mid_index - 1] + sorted_arr[mid_index]) // 2

# Let's test the code
estimate_finder = MiddleElementFinder()
estimate_finder.add_num(5)
estimate_finder.add_num(10)
estimate_finder.add_num(3)
estimate_finder.add_num(1)
estimate_finder.add_num(7)

print(estimate_finder.middle_element()) # Expected output: 5
print(estimate_finder.naive_middle_element())
