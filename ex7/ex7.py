import timeit

from matplotlib import pyplot as plt

def binary_search(arr, key, start, end, mid = 0):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start + 1

    if start > end:
        return start
    if mid == 0:
        mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid - 1)
    else:
        return mid

import json
if __name__ == '__main__':
    with open('./ex7/ex7data.json') as f:
        data = json.load(f)
    with open('./ex7/ex7tasks.json') as f:
        tasks = json.load(f)
    chosen_MidPoints = []
    print(len(data))
    print(len(tasks))
    for i in range(0, len(tasks)):
        arrTimeit = []
        midPointLowerBound = int(tasks[i]) - (len(data)//8)
        midPointUpperBound = int(tasks[i]) + (len(data)//8)
        if midPointLowerBound < 0:
            midPointLowerBound = 0
        if midPointUpperBound > len(data):
            midPointUpperBound = len(data)
        for j in range(int(midPointLowerBound), int(midPointUpperBound), 10000):
            arrTimeit.append([timeit.timeit(lambda: binary_search(data, j, 0, len(data) - 1), number=100),j])
        chosen_MidPoints.append([tasks[i], min(arrTimeit, key=lambda x: x[0])[1]])
    
    print(chosen_MidPoints)

    plt.scatter([x[0] for x in chosen_MidPoints], [x[1] for x in chosen_MidPoints])
    plt.xlabel('Task')
    plt.ylabel('Chosen Midpoint')
    plt.savefig('./img/' + 'ex7' + '.png')
    plt.show()
    print('done')
    '''
    4.  the choice of initial midpoint does appear to affect performance. 
    The choice of initial midpoint is important because it affects the number of iterations the binary search algorithm will have to go through to find the key. 
    If the initial midpoint is too far from the key, the algorithm will have to go through more iterations to find the key. 
    If the initial midpoint is too close to the key, the algorithm will have to go through fewer iterations to find the key. 
    '''



