import random
import matplotlib.pyplot as plt
import timeit
import numpy as np



def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Function for linear search



def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
# Function for binary search


def generate_random_array(max_val):
    array = list(range(max_val))
    np.random.shuffle(array)
    
    return array
# Function to generate a randomly shuffled array


def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)
# Function to perform the QuickSort algorithm


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    
    return i + 1
# Function to partition array for the QuickSort algorithm


def sort_and_search(arr, task):
    quick_sort(arr, 0, len(arr) - 1)
    
    return binary_search(arr, task)
# Function to sort array and perform binary search





linear_times = []
sort_and_search_times = []
# Lists to store timing information

input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000] 
# List of input sizes for analysis


# Loop through each input size
for input_size in input_sizes:

   
    if input_size <= 0:
        linear_time = 0
        sort_n_search_time = 0
    # Check if input size is valid

    else:
        # Random array
        unsorted_array = generate_random_array(input_size)

        # random index for the search task
        rand_index = random.randint(0, len(unsorted_array) - 1)
        task = unsorted_array[rand_index]
        linear_time = 0
        sort_n_search_time = 0
        print(f"Analyzing Time Complexity with {input_size} entries...")

        
        for i in range(101):
            linear_time_i = 0
            sort_n_search_time_i = 0
            for _ in range(100):
                # Perform 100 runs for averaging

                
                linear_time_i += timeit.timeit(lambda: linear_search(unsorted_array, task), number=1)
                #Time measure Linear search
                
                sort_n_search_time_i += timeit.timeit(lambda: sort_and_search(unsorted_array, task), number=1)
                # Time measure for sorting and binary search
                
                np.random.shuffle(unsorted_array)
                # Shuffle array 
            
            
            
            linear_time += linear_time_i / 100
            sort_n_search_time += sort_n_search_time_i / 100
            # Accumulate timing information

    # Calculate average timing for linear search
    linear_times.append(linear_time / 100)

    # Calculate average timing for sorting and binary search
    sort_and_search_times.append(sort_n_search_time / 100)
    

plt.plot(input_sizes, linear_times, label='Linear Search Timings')
plt.plot(input_sizes, sort_and_search_times, label='Sort + Search Times')
# Plotting the results


plt.title('Time Complexity Analysis Graph')
plt.xlabel('Input Sizes')
plt.ylabel('Time (Seconds)')
plt.legend()
# Adding labels and title to the plot

plt.savefig("ex6_avg.jpg")

