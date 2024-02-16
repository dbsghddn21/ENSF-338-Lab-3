import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import timeit
import random
import copy

import sys
sys.setrecursionlimit(16000)

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
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
    plt.plot(listsize, times, x, func(x, *popt), '-')
    plt.title(title)
    plt.savefig(title + '.png')
    plt.show()
def plotQuickVersusBubble(listsize, timeitBubbleSortAvg, timeitQuickSortAvg, poptBS, pcovBS, poptQS, pcovQS, func1, func2,title):
    x = np.linspace(min(listsize), max(listsize), num=100, endpoint=True)
    plt.plot(listsize, timeitBubbleSortAvg, x, func1(x, *poptBS), '-', label='Bubble Sort')
    plt.plot(listsize, timeitQuickSortAvg, x, func2(x, *poptQS), '-', label='Quick Sort')
    plt.legend()
    plt.xlabel('List Size')
    plt.ylabel('Time')

    plt.title(title)
    plt.savefig(title + '.png')
    plt.show()
def sortRegardListSize(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) <2000:
        return bubblesort(arr)
    else:
        return quicksort(arr)
    
    
    

if __name__ == '__main__':
    Arrlen = []
    arrofArrays = []
    for i in range(20):
        Arrlen.append(np.random.randint(0, 1000, 1))
    Arrlen_np = np.array(Arrlen)
    sortedArrlen = sorted(Arrlen_np, key=lambda x: x[0])
    for i in sortedArrlen:
        arrofArrays.append(list(np.random.choice(np.arange(1,i*2), i, replace=False)))
    print(sys.getrecursionlimit())
    sortedArrays = []
    for i in arrofArrays:
        sortedArrays.append(list(np.sort(i)))

    reversedSortedArrays = []
    for i in sortedArrays:
        reversedSortedArrays.append(i[::-1])

    timeitBubbleSortAvg = []
    timeitQuickSortAvg = []
    for i in range(20):
        print('List ',i,' : List Size :', len(arrofArrays[i]))
        arrCopy = copy.deepcopy(arrofArrays[i])
        timeitBubbleSortAvgtemp = []
        timeitQuickSortAvgtemp = []
        for j in range(100):
            random.shuffle(arrCopy)
            timeitBubbleSortAvgtemp.append(timeit.timeit(lambda: bubblesort(arrCopy),number=1))
            random.shuffle(arrCopy)
            timeitQuickSortAvgtemp.append(timeit.timeit(lambda: quicksort(arrCopy), number=1))
        timeitBubbleSortAvg.append(sum(timeitBubbleSortAvgtemp))
        print('Bubble Sort Average Time:', timeitBubbleSortAvg[-1])
        timeitQuickSortAvg.append(sum(timeitQuickSortAvgtemp))
        print('Quick Sort Average Time:', timeitQuickSortAvg[-1])

    
    timeitBubbleSortBest = []
    timeitQuickSortBestSorted = []
    for i in range(20):
        timeitBSBTemp = []
        timeitQSBTemp = []
        for j in range(100):
            arrCopy = copy.deepcopy(sortedArrays[i])
            timeitBSBTemp.append(timeit.timeit(lambda: bubblesort(arrCopy), number=1))
            arrCopy = copy.deepcopy(arrofArrays[i])
            random.shuffle(arrCopy)
            timeitQSBTemp.append(timeit.timeit(lambda: quicksort(arrCopy), number=1))
        timeitBubbleSortBest.append(sum(timeitBSBTemp))
        print('Bubble Sort Best Time:', timeitBubbleSortBest[-1])
        timeitQuickSortBestSorted.append(sum(timeitQSBTemp))
        print('Quick Sort Best Time:', timeitQuickSortBestSorted[-1])


    timeitBubbleSortWorst = []
    timeitQuickSortWorst = []
    for i in range(20):
        timeitBSWTemp = []
        timeitQSWTemp = []
        for j in range(100):
            arrCopy = copy.deepcopy(reversedSortedArrays[i])
            timeitBSWTemp.append(timeit.timeit(lambda: bubblesort(arrCopy), number=1))
            arrCopy = copy.deepcopy(reversedSortedArrays[i])
            timeitQSWTemp.append(timeit.timeit(lambda: quicksort(arrCopy), number=1))
        timeitBubbleSortWorst.append(sum(timeitBSWTemp))
        print('Bubble Sort Worst Time:', timeitBubbleSortWorst[-1])
        timeitQuickSortWorst.append(sum(timeitQSWTemp))
        print('Quick Sort Worst Time:', timeitQuickSortWorst[-1])
    listsize = []
    for i in range(20):
        listsize.append(len(arrofArrays[i]))
    
    def qudratic(n, a, b, c):
        return a*n**2 + b*n + c
    def nlogn(n, a, b):
        return a*n*np.log(n) + b
    def linear(n ,a, b):
        return a*n + b
    
    popt_BSA, pcov_BSA = curve_fit(qudratic, listsize, timeitBubbleSortAvg) #bubble sort average case
    popt_QSA, pcov_QSA = curve_fit(nlogn, listsize, timeitQuickSortAvg) #quick sort average case
    popt_BSB, pcov_BSB = curve_fit(linear, listsize, timeitBubbleSortBest) #bubble sort best case
    popt_QSB, pcov_QSB = curve_fit(nlogn, listsize, timeitQuickSortBestSorted) #quick sort best case
    popt_BSW, pcov_BSW = curve_fit(qudratic, listsize, timeitBubbleSortWorst) #bubble sort worst case
    popt_QSW, pcov_QSW = curve_fit(qudratic, listsize, timeitQuickSortWorst) #quick sort worst case

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
    interpolateAndPlot(listsize, timeitBubbleSortBest, popt_BSB, pcov_BSB, linear, 'Bubble Sort Best Case')
    interpolateAndPlot(listsize, timeitQuickSortBestSorted, popt_QSB, pcov_QSB, nlogn, 'Quick Sort Best Case')
    interpolateAndPlot(listsize, timeitBubbleSortWorst, popt_BSW, pcov_BSW, qudratic, 'Bubble Sort Worst Case')
    interpolateAndPlot(listsize, timeitQuickSortWorst, popt_QSW, pcov_QSW, qudratic, 'Quick Sort Worst Case')

    plotQuickVersusBubble(listsize, timeitBubbleSortAvg, timeitQuickSortAvg, popt_BSA, pcov_BSA, popt_QSA, pcov_QSA, qudratic, nlogn, 'Versus Average Case')
    plotQuickVersusBubble(listsize, timeitBubbleSortBest, timeitQuickSortBestSorted, popt_BSB, pcov_BSB, popt_QSB, pcov_QSB, linear, nlogn, 'Versus Best Case')
    plotQuickVersusBubble(listsize, timeitBubbleSortWorst, timeitQuickSortWorst, popt_BSW, pcov_BSW, popt_QSW, pcov_QSW, qudratic, qudratic, 'Versus Worst Case')




    
    

    
