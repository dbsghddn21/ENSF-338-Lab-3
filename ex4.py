import numpy as np
import matplotlib.pyplot as plt
import time
import random
from scipy.optimize import curve_fit

def quickSort(vector):
    if len(vector) <= 1:
        return vector
    else:
        pivot = max(vector)
        less = [x for x in vector if x < pivot]
        equal = [x for x in vector if x == pivot]
        greater = [x for x in vector if x > pivot]
        sorted_vector = quickSort(less) + equal + quickSort(greater)
        #print("Current state of vector:", sorted_vector) #uncomment to see the state of the vector at each iteration
        return sorted_vector

def random16vec():
    vector = [random.randint(1, 100) for _ in range(16)]
    print("Original vector:", vector)
    sorted_vector = quickSort(vector)
    print("Sorted vector:", sorted_vector)

if __name__ == "__main__":
    #random16vec()
    sizes = []
    timeQuick = []
    
    for n in range(100, 3100, 100):
        arr = [random.randint(0, 1000) for _ in range(n)]  # Generate n random numbers
        start_time = time.time()
        quickSort(arr.copy())  # Use a copy to not affect the original array
        end_time = time.time()
        timeQuick.append(end_time - start_time)
        sizes.append(n)
    
    def quadratic(x, a, b, c):
        return a * x ** 2 + b * x + c
    
    popt, pcov = curve_fit(quadratic, sizes, timeQuick)

    plt.figure(figsize=(12, 6))
    plt.plot(sizes, timeQuick, label='Quick Sort')
    plt.plot(sizes, quadratic(np.array(sizes), *popt), label='Fitted Quadratic', linestyle='--')
    plt.xlabel('Vector size')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig('quickSort.png')
    plt.show()
    