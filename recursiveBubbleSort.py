## Sorting
## In each pass, push the largest element to the end.

def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    # Base case: if the array size is 1, it's sorted
    if n == 1:
        return

    # One pass to move the largest to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call to bubble sort the remaining array
    recursive_bubble_sort(arr, n - 1)

    return arr
    


arr = [2,4,5,8,4,3] 
print(recursive_bubble_sort(arr))
