import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
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

def interpolateAndPlot(listsize, times, popt, pcov, func, title):
    x = np.linspace(min(listsize), max(listsize), num=100, endpoint=True)
    plt.plot(listsize, times, xnew, func(xnew, *popt), '-')
    plt.title(title)
    plt.savefig(title + '.png')
    plt.show()

    
    

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
    
    timeitBubbleSortBest = []
    timeitQuickSortBestSorted = []
    for i in range(20):
        timeitBubbleSortBest.append(timeit.timeit(lambda: bubblesort(sortedArrays[i]), number=100)/100)
        timeitQuickSortBestSorted.append(timeit.timeit(lambda: quicksort(arrofArrays[i]), number=100)/100)

    timeitBubbleSortWorst = []
    timeitQuickSortWorst = []
    for i in range(20):
        timeitBubbleSortWorst.append(timeit.timeit(lambda: bubblesort(reversedSortedArrays[i]), number=100)/100)
        timeitQuickSortWorst.append(timeit.timeit(lambda: quicksort(reversedSortedArrays[i]), number=100)/100)

    listsize = []
    for i in range(20):
        listsize.append(len(arrofArrays[i]))
    
    def qudratic(n, a, b, c):
        return a*n**2 + b*n + c
    def nlogn(n, a, b):
        return a*n*np.log(n) + b
    def linear(n ,a, b):
        return a*n + b
    
    popt_BSA, pcov_BSA = curve_fit(qudratic, listsize, timeitBubbleSortAvg)
    popt_QSA, pcov_QSA = curve_fit(nlogn, listsize, timeitQuickSortAvg)
    popt_BSB, pcov_BSB = curve_fit(qudratic, listsize, timeitBubbleSortBest)
    popt_QSB, pcov_QSB = curve_fit(nlogn, listsize, timeitQuickSortBestSorted)
    popt_BSW, pcov_BSW = curve_fit(qudratic, listsize, timeitBubbleSortWorst)
    popt_QSW, pcov_QSW = curve_fit(nlogn, listsize, timeitQuickSortWorst)

    print('Bubble Sort Average Case')
    for i in range(20):
        print('List ',i,' : List Size :', listsize[i], 'Time:', timeitBubbleSortAvg[i])
    print('Bubble Sort Best Case')
    for i in range(20):
        print('List ',i,' : List Size :', listsize[i], 'Time:', timeitBubbleSortBest[i])
    print('Bubble Sort Worst Case')
    for i in range(20):
        print('List ',i,' : List Size :', listsize[i], 'Time:', timeitBubbleSortWorst[i])
    print('Quick Sort Average Case')
    for i in range(20):
        print('List ',i,' : List Size :', listsize[i], 'Time:', timeitQuickSortAvg[i])
    print('Quick Sort Best Case')
    for i in range(20):
        print('List ',i,' : List Size :', listsize[i], 'Time:', timeitQuickSortBestSorted[i])
    print('Quick Sort Worst Case')
    for i in range(20):
        print('List ',i,' : List Size :', listsize[i], 'Time:', timeitQuickSortWorst[i])
    interpolateAndPlot(listsize, timeitBubbleSortAvg, popt_BSA, pcov_BSA, qudratic, 'Bubble Sort Average Case')
    interpolateAndPlot(listsize, timeitQuickSortAvg, popt_QSA, pcov_QSA, nlogn, 'Quick Sort Average Case')
    interpolateAndPlot(listsize, timeitBubbleSortBest, popt_BSB, pcov_BSB, qudratic, 'Bubble Sort Best Case')
    interpolateAndPlot(listsize, timeitQuickSortBestSorted, popt_QSB, pcov_QSB, nlogn, 'Quick Sort Best Case')
    interpolateAndPlot(listsize, timeitBubbleSortWorst, popt_BSW, pcov_BSW, qudratic, 'Bubble Sort Worst Case')
    interpolateAndPlot(listsize, timeitQuickSortWorst, popt_QSW, pcov_QSW, nlogn, 'Quick Sort Worst Case')




    
    

    
