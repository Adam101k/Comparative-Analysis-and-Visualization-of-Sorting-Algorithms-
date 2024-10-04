# Bubble Sort Algorithm
# Input: An array of integers `arr`.
# Bubble Sort is a simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements,
# and swaps them if they are in the wrong order. This process is repeated until the array is sorted.
# Time Complexity: O(n^2), where n is the number of elements, as the algorithm has two nested loops.
# Space Complexity: O(1), as it performs sorting in-place without any extra memory allocation.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

# Merge Sort Algorithm
# Input: An array `arr` to be sorted.
# Merge Sort is a divide-and-conquer algorithm that recursively splits the array into halves, sorts each half,
# and then merges the sorted halves.
# Time Complexity: O(n log n), where n is the number of elements in the array.
# Space Complexity: O(n), as it requires additional space for the temporary arrays used during merging.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        yield from merge_sort(left_half)
        yield from merge_sort(right_half)

        i = j = k = 0

        # Merging the sorted halves back into the array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            yield arr

        # If there are any remaining elements in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            yield arr

        # If there are any remaining elements in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            yield arr

# Partition function for Quick Sort
# Input: An array of integers `arr`, and two indices `low` and `high` representing the portion of the array to partition.
# The function selects a pivot (the last element), places all elements smaller than the pivot on its left,
# and all elements greater than the pivot on its right, effectively partitioning the array relative to the pivot.
# Time Complexity: O(n), where n is the number of elements between `low` and `high`.
# Space Complexity: O(1), since it operates in place without needing additional memory.
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # Pointer for the greater element
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick Sort Algorithm
# Input: An array of integers `arr`, with indices `low` and `high` representing the portion of the array to sort.
# Quick Sort uses a divide-and-conquer approach by selecting a pivot element and recursively sorting the subarrays
# to the left and right of the pivot.
# Time Complexity: O(n log n) on average, where n is the number of elements, but O(n^2) in the worst case (e.g., when the array is already sorted or reverse sorted).
# Space Complexity: O(log n) due to the recursive stack space in the average case, O(n) in the worst case due to recursion depth.
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition the array
        yield arr
        yield from quick_sort(arr, low, pi - 1)  # Sort the left subarray
        yield from quick_sort(arr, pi + 1, high)  # Sort the right subarray

# Counting Sort Function
# Input: An array `arr` and a base (digit position) `base` for sorting based on a particular place value.
# Counting Sort is a non-comparison-based algorithm that sorts the array by counting the occurrences of each digit
# in a particular place and placing elements in the correct order.
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(n + k), where n is the number of elements, and k is the range of digits (in this case, 10).
def counting_sort(arr, base):
    size = len(arr)
    output = [0] * size  # Output array to store sorted values
    count = [0] * 10  # Initialize count array for digits 0-9

    # Counting how often each digit appears in the current place value
    for i in range(size):
        index = arr[i] // base  # Extract the digit
        count[index % 10] += 1

    # Calculate actual positions of each digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the sorted output array
    for i in range(size - 1, -1, -1):
        index = arr[i] // base
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    # Copy the sorted array back into the original array
    for i in range(size):
        arr[i] = output[i]
        yield arr

# Radix Sort Algorithm
# Input: An array of integers `arr`.
# Radix Sort is a non-comparison-based algorithm that sorts elements digit by digit starting from the least significant
# digit to the most significant digit using Counting Sort as a subroutine.
# Time Complexity: O(n * d), where n is the number of elements and d is the number of digits in the largest number.
# Space Complexity: O(n + k), where n is the number of elements and k is the range of digits (for counting sort).
def radix_sort(arr):
    my_max = max(arr)
    base = 1
    while my_max // base > 0:  # Process each digit place value
        yield from counting_sort(arr, base)
        base *= 10

# Linear Search Algorithm
# Input: An array of integers `arr` and a `target` value to search for.
# Time Complexity: O(n), where n is the number of elements in the array.
def linear_search(arr, target):
    # Iterate through the array to search for the target number
    for i in range(len(arr)):
        if arr[i] == target:
            yield i  # Yield the current index being checked when target is found
            return
        else:
            yield i  # Still yield the index for each step to visualize the progress



