import random

def find_kth_largest(numbers, k):
    if numbers:
        # implement this
        pos = partition(numbers, 0, len(numbers) - 1)
        if k - 1 == pos:
            # The pivot is the k-th element after partitioning
            return numbers[pos]
        elif k - 1 < pos:
            # The pivot index after partitioning is larger than k
            # We'll keep searching in the left part
            return find_kth_largest(numbers[:pos], k)
        else:
            # The pivot index after partitioning is smaller than k
            # We'll keep searching in the right part
            return find_kth_largest(numbers[pos + 1:], k - pos - 1)

def partition(nums, l, r):
    # Choosing a random index to make the algorithm less deterministic
    rand_index = random.randint(l, r)
    nums[l], nums[rand_index] = nums[rand_index], nums[l]
    pivot_index = l
    for i in range(l + 1, r + 1):
        if nums[i] >= nums[l]:
            pivot_index += 1
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
    nums[pivot_index], nums[l] = nums[l], nums[pivot_index]
    return pivot_index


print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # Expected output: 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Expected output: 4
