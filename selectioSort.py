## Sorting

def selectionSort(arr):
    
    for i in range(len(arr)-1):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[mini]:
                mini = j
            
        arr[i], arr[mini] = arr[mini], arr[i]

    return arr

arr = [2,4,5,8,4, 3,3] 
print(selectionSort(arr))
