import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_search(arr, key, start, end):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid - 1)
    else:
        return mid
    
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr[0:i], key, 0, i-1)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr
    
sizes = []
timesInsertion = []
timesInsertionBinary = []

for n in range(100, 1100, 100):
    arr = [random.randint(0, 1000) for _ in range(n)]  # Generate n random numbers

    start_time = time.time()
    insertion_sort(arr.copy())  # Use a copy to not affect the original array
    end_time = time.time()
    timesInsertion.append(end_time - start_time)

    start_time = time.time()
    binary_insertion_sort(arr.copy())  # Use a copy to not affect the original array
    end_time = time.time()
    timesInsertionBinary.append(end_time - start_time)

    sizes.append(n)

plt.figure(figsize=(12, 6))
plt.plot(sizes, timesInsertion, label='Insertion Sort')
plt.plot(sizes, timesInsertionBinary, label='Binary Insertion Sort')
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.savefig('ex5.png')
plt.show()
'''

The binary insertion sort is faster than the regular insertion sort for larger input sizes. 
This is because the binary insertion sort uses binary search to find the correct position for the current element,
which is O(log n), while the regular insertion sort uses a linear search to find the correct position, which is O(n).
Therefore, the binary insertion sort is faster for larger input sizes.
'''