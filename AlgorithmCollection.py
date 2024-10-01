# This will be where the collection of Alogirthms will be stored

# Bubble Sort Algorithm
# Input: An array `arr` of integers to be sorted.
# Bubble Sort repeatedly steps through the array, compares adjacent elements, and swaps them if they are in the wrong order.
# The process repeats until the entire array is sorted. 
# Time complexity: O(n^2) in the worst and average case due to the nested loops, making it inefficient for large datasets.
def bubble_sort(arr):

    # Get the length of the array
    n = len(arr)

    # Outer loop runs n times (where n is the length of the array).
    # With each pass, the largest unsorted element "bubbles" to the correct position.
    for i in range(n):
        
        # Inner loop runs from 0 to n-i-1 because after each iteration of the outer loop,
        # the last i elements are already sorted, so they don't need to be checked again.
        for j in range(0, n-i-1):
            
            # Compare the current element with the next one
            # If the current element is greater, swap it with the next element.
            if arr[j] > arr[j+1]:
                # Swap the elements to put them in correct order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # Return the sorted array
    return arr


# Merge Sort Algorithm
# Input: An array `arr` to be sorted, with indices `left` and `right` representing the portion of the array to sort.
# The merge_sort function is a divide-and-conquer algorithm that recursively splits the array into halves, sorts each half,
# and then merges the sorted halves. The total time complexity is O(n log n), where n is the number of elements in the array.
def merge_sort(arr, left, right):
    # Base case: If the length of the array is more than 1, proceed with sorting
    if len(arr) > 1:
        # Find the middle index of the array
        mid = len(arr) // 2
        
        # Split the array into two halves: left and right
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursively apply merge_sort to the left half
        merge_sort(left, 0, len(left))
        # Recursively apply merge_sort to the right half
        merge_sort(right, 0, len(right))

        # Merge the two sorted halves into one sorted array
        arr = merge(left, right)
    
    # Return the sorted array
    return arr
    


# Merge function to combine two sorted arrays
# Input: Two sorted arrays `left` and `right`, which are parts of the original array
# The merge function merges the two sorted arrays into a single sorted array.
# The time complexity of this function is O(n), where n is the total number of elements in `left` and `right`.
def merge(left, right):
    # Initialize an empty result array to hold the merged output
    result = []
    
    # Initialize two pointers for iterating over left and right arrays
    i = j = 0
    
    # Continue comparing elements of left and right arrays until one of them is exhausted
    while i < len(left) and j < len(right):
        # If the current element in the left array is smaller, add it to the result
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        # Otherwise, add the current element in the right array to the result
        else:
            result.append(right[j])
            j += 1
    
    # After the loop, append any remaining elements from the left array (if any)
    result += left[i:]
    
    # Append any remaining elements from the right array (if any)
    result += right[j:]
    
    # Return the merged and sorted array
    return result

# Partition function to divide the array based on the pivot
# Input: An array of integers, and two indices `low` and `high` representing the current portion of the array to partition.
# The function selects a pivot (the last element), places all elements smaller than the pivot on its left,
# and all elements greater than the pivot on its right, effectively "sorting" the array relative to the pivot.
# Time complexity: O(n) where n is the number of elements between `low` and `high`.
def partition(arr, low, high):

    # Choose the rightmost element as the pivot
    pivot = arr[high]

    # Initialize pointer for the greater element (i starts before the first element)
    i = low - 1

    # Traverse the array from `low` to `high-1`
    # Compare each element with the pivot
    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot, swap it with the element at index `i`
        if arr[j] <= pivot:
            i = i + 1
            # Swap the current element `j` with the element at index `i` (places smaller elements on the left)
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the element at index `i+1` to place the pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the index where the partitioning happened
    return i + 1


# Quick Sort Algorithm
# Input: An array of integers `arr`, with indices `low` and `high` representing the portion of the array to sort.
# Quick Sort uses a divide-and-conquer approach by selecting a pivot element and recursively sorting the subarrays
# to the left and right of the pivot. 
# Time complexity: O(n log n) on average, where n is the number of elements, but O(n^2) in the worst case (e.g., when the array is already sorted or reverse sorted).
def quick_sort(arr, low, high):
    
    # Perform quicksort only if the `low` index is less than the `high` index
    if low < high:
        # Find the pivot position where the array is partitioned into two halves
        pi = partition(arr, low, high)

        # Recursively apply quicksort to the left half (elements smaller than the pivot)
        quick_sort(arr, low, pi - 1)

        # Recursively apply quicksort to the right half (elements greater than the pivot)
        quick_sort(arr, pi + 1, high)
