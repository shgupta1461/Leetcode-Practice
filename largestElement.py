## Largest element in array

def largestElement(arr):
    largest = arr[0]
    
    for i in range(1, len(arr)):

        if arr[i] > largest:
            largest = arr[i]
    
    return largest



arr = [2,4,5,8,4,3] 
print(largestElement(arr))
