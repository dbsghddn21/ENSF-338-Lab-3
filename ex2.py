import numpy as np
import matplotlib.pyplot as plt
import timeit
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [i for i in arr[:-1] if i <= pivot]
    right = [i for i in arr[:-1] if i > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == '__main__':
    arrofArrays = []
    for i in range(20):
        arrofArrays.append(np.random.randint(0, 16000, 1))
    j = 0
    arrofArrays = np.sort(arrofArrays)
    for i in arrofArrays:
        arrofArrays[j] = np.random.choice(np.arange(1,i*2), i, replace=False)
        j += 1

    sortedArrays = []
    for i in arrofArrays:
        sortedArrays.append(np.sort(i))

    reversedSortedArrays = []
    for i in sortedArrays:
        reversedSortedArrays.append(i[::-1])

    timeitBubbleSortAvg = []
    timeitQuickSortAvg = []
    for i in range(20):
        timeitBubbleSortAvg.append(timeit.timeit(lambda: bubblesort(arrofArrays[i]), number=100)/100)
        timeitQuickSortAvg.append(timeit.timeit(lambda: quicksort(arrofArrays[i]), number=100)/100)
    
    timeitBubbleSortBestSorted = []
    timeitQuickSortBestSorted = []
    for i in range(20):
        timeitBubbleSortBestSorted.append(timeit.timeit(lambda: bubblesort(sortedArrays[i]), number=100)/100)
        timeitQuickSortBestSorted.append(timeit.timeit(lambda: quicksort(arrofArrays[i]), number=100)/100)

    timeitBubbleSortWorstSorted = []
    timeitQuickSortWorstSorted = []
    for i in range(20):
        timeitBubbleSortWorstSorted.append(timeit.timeit(lambda: bubblesort(reversedSortedArrays[i]), number=100)/100)
        timeitQuickSortWorstSorted.append(timeit.timeit(lambda: quicksort(reversedSortedArrays[i]), number=100)/100)
