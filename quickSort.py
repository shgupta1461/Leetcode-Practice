## Sorting
## Pick a pivot element, use two pointers i, j to partition the array 
## and then recursively run quicksort on left and right partition.
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i = i+1
        
        while arr[j]>pivot and j>=low+1:
            j = j-1

        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr, low, high):
    
    if low<high:
        partition_index = partition(arr, low, high)
        quickSort(arr, low, partition_index-1)
        quickSort(arr, partition_index+1, high)



arr = [2,4,5,8,4,3] 
low = 0
high = len(arr)-1
quickSort(arr, low, high)
print(arr)
