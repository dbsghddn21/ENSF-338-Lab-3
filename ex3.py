import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    comparisonsCount = 0
    swapsCount = 0

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapsCount += 1
            comparisonsCount += 1
    return arr, comparisonsCount, swapsCount

sizes = []
times = []
comparisons = []
swaps = []

# Generate arrays of increasing size (from 100 to 1000 elements)
for n in range(100, 1100, 100):
    arr = [random.randint(0, 1000) for _ in range(n)]  # Generate n random numbers
    start_time = time.time()
    sorted_arr, comparison, swap = bubble_sort(arr)
    end_time = time.time()
    sizes.append(n)
    times.append(end_time - start_time)
    comparisons.append(comparison)
    swaps.append(swap)

# Plot comparisons and swaps by input size
plt.figure(figsize=(12, 6))
plt.plot(sizes, comparisons, label='Comparisons')
plt.plot(sizes, swaps, label='Swaps')
plt.xlabel('Input size')
plt.ylabel('Count')
plt.legend()
plt.savefig('ex3.png')
plt.show()