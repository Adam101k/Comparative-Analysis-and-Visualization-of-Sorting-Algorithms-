#Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr [j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

# Merge Sort
# Input: An array `arr` to be sorted.
# The merge_sort function is a divide-and-conquer algorithm that recursively splits the array into halves, sorts each half,
# and then merges the sorted halves. The total time complexity is O(n log n), where n is the number of elements in the array.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        yield from merge_sort(left_half)
        yield from merge_sort(right_half)

        i = j = k = 0

        while i< len(left_half) and j < len(right_half):
            if left_half[i] < right_half [j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            yield arr

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            yield arr

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            yield arr

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
        yield arr
        # Recursively apply quicksort to the left half (elements smaller than the pivot)
        yield from quick_sort(arr, low, pi - 1)

        # Recursively apply quicksort to the right half (elements greater than the pivot)
        yield from quick_sort(arr, pi + 1, high)


#counting function in order to sort the array based on our current number place.
def counting_sort(arr, base):
    size = len(arr) 
    output = [0] * size
    count = [0] * 10

    #Counting how often our nth place number occurs
    for i in range(0, size):
        index = arr[i] // base #index is our number based on what nth place we are currently at
        count[index % 10] += 1

    #Making count[i] have the actual position of the digits in the output array.
    for i in range (1, 10):
        count[i] += count[i - 1]
    
    #Filling out output array with our input array based on the position of our nth place base
    for i in range(size -1, -1, -1):
        index = arr[i] // base
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    #Copy the sorted array to our input array
    for i in range(size):
        arr[i] = output[i]
        yield arr

#Radix Sort Algorithm
#Input: An array of integers
#Time Complexity: O(n*d)
#n is how many elements in our array
#d is how many digits there are in our largest number
def radix_sort(arr):
    my_max = max(arr)
    base = 1
    while my_max / base >= 1:
        yield from counting_sort(arr, base)
        base *= 10


#Linear Search Algorithm
#Input: An array of integers and the target number in which we want to find.
#Time Complexity: O(n) where n is the number of elements in our array. 
#def linear_search(arr, target):
    #Gets the time when algorithm started
    #holder will hold all of the index for the number we want
#    holder = []

    #Iterate through our array of integers to search for our target number.
#    for i in range(len(arr)):
#        if arr[i] == target:
#            holder.append(i)
#        else:
#            holder.append(-1)