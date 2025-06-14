## Sorting

def insertionSort(arr):
    
    for i in range(len(arr)):
        j = i
        while j>0 and arr[j]<arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1
    
    return arr

arr = [2,4,5,8,4, 3,3] 
print(insertionSort(arr))
