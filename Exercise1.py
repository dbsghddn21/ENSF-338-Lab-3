def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
        
        
def merge(arr, low, mid, high):
    
    subarray1 = mid - low + 1
    subarray2 = high - mid
    
    i = 0
    j = 0
    z = low
    
    leftarr = arr[low:low + subarray1]
    rightarr = arr[mid + 1:mid + 1 + subarray2]
    
    while i < subarray1 and j < subarray2:
        if leftarr[i] <= rightarr[j]:
            arr[z] = leftarr[i]
            i = i + 1
        else:
            arr[z] = rightarr[j]
            j = j + 1
            z = z + 1
    
    while i < subarray1:
        arr[z] = leftarr[i]
        i += 1
        z += 1
        
    while j < subarray2:
        arr[z] = rightarr[j]
        j += 1
        z += 1
            
    