import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Generate a list of 20 random numbers between 50 and 100
random_numbers = [random.randint(50, 100) for _ in range(20)]
print("Unsorted List: ", random_numbers)

# TODO: Use the Quick Sort function to sort the list in descending order and print the sorted list
sorted_numbers = quick_sort(random_numbers)
print("Sorted List: ", sorted_numbers)
