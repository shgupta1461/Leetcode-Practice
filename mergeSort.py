## Sorting
## We recursively split the array, and go from top-down until all sub-arrays size becomes 1.
## merge(): This function is used to merge the 2 halves of the array. 
## It assumes that both parts of the array are sorted and merges both of them.
## mergeSort(): This function divides the array into 2 parts. low to mid and mid+1 to high

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1

    while(left<=mid and right<=high):
        if arr[left]<= arr[right]:
            temp.append(arr[left])
            left = left + 1
            
        else:
            temp.append(arr[right])
            right = right + 1

    while left<=mid:
        temp.append(arr[left])
        left = left + 1

    while right<=high:
        temp.append(arr[right])
        right = right + 1

    for i in range(low, high+1):
        arr[i] = temp[i-low]

def mergeSort(arr, low, high):
    
    mid = int((low + high)//2) 
    
    if low>=high:
        return
    
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)

    merge(arr, low, mid, high)


arr = [2,4,5,8,4,3] 
low = 0
high = len(arr)-1
mergeSort(arr, low, high)
print(arr)
