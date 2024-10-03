import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time


def bubble_sort(arr, update_visualization, pause_flag, after_function):
    n = len(arr)
    i = 0  # Outer loop index

    def sort_step():
        nonlocal i
        if i < n:
            j = 0
            while j < n - i - 1:
                if not pause_flag[0]:
                    return  # If paused, exit and stop further sorting until resumed

                # Swap if the current element is greater than the next
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Update the visualization
                update_visualization(arr)
                j += 1
            
            i += 1  # Move to the next pass
            after_function(100, sort_step)  # Schedule the next step with Tkinter's after
        else:
            update_visualization(arr)  # Final visualization when sorting is complete

    sort_step()  # Start sorting process





# Merge Sort Algorithm
# Input: An array `arr` to be sorted.
# The merge_sort function is a divide-and-conquer algorithm that recursively splits the array into halves, sorts each half,
# and then merges the sorted halves. The total time complexity is O(n log n), where n is the number of elements in the array.
def merge_sort(arr):
    # Base case: If the length of the array is less than or equal to 1, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle index of the array
    mid = len(arr) // 2
    
    # Split the array into two halves: left and right
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively apply merge_sort to the left and right halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the two sorted halves into one sorted array
    return merge(left_sorted, right_sorted)


# Merge function to combine two sorted arrays
# Input: Two sorted arrays `left` and `right`, which are parts of the original array.
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


#counting function in order to sort the array based on our current number place.
def counting_sort(array, base):
    size = len(array) 
    output = [0] * size
    count = [0] * 10

    #Counting how often our nth place number occurs
    for i in range(0, size):
        index = array[i] // base #index is our number based on what nth place we are currently at
        count[index % 10] += 1

    #Making count[i] have the actual position of the digits in the output array.
    for i in range (1, 10):
        count[i] += count[i - 1]
    
    #Filling out output array with our input array based on the position of our nth place base
    for i in range(size -1, -1, -1):
        index = array[i] // base
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    #Copy the sorted array to our input array
    for i in range(size):
        array[i] = output[i]

#Radix Sort Algorithm
#Input: An array of integers
#Time Complexity: O(n*d)
#n is how many elements in our array
#d is how many digits there are in our largest number
def radix_sort(array):
    start = time.time()
    my_max = max(array)
    base = 1
    while my_max / base >= 1:
        counting_sort(array, base)
        base *= 10
    end = time.time()
    algorithm_time = end - start
    return algorithm_time, array


#Linear Search Algorithm
#Input: An array of integers and the target number in which we want to find.
#Time Complexity: O(n) where n is the number of elements in our array. 
def linear_search_algorithm(array, target):
    #Gets the time when algorithm started
    start = time.time()
    #holder will hold all of the index for the number we want
    holder = []

    #Iterate through our array of integers to search for our target number.
    for i in range(len(array)):
        if array[i] == target:
            holder.append(i)
    #Gets the time when the algorithm is done
    end = time.time()
    #Math for how long the algorithm took
    algorithm_time = end - start
    #If target is not found, we return the time of our algorithm and -1.
    if(len(holder) == 0):
        return algorithm_time, -1
    else:
        #if at least one target is found, we return the time and the list of indices containing our target.
        return algorithm_time, holder
