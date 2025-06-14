## Sorting

def bubbleSort(arr):
    
    for i in range(len(arr)):
        j = i
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

arr = [2,4,5,8,4, 3,3] 
print(bubbleSort(arr))
