## Sorting
## Takes last element of sub array and place it in its corect position

def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)
    
    # Base case: if array size is 1 or 0, it's already sorted
    if n <= 1:
        return arr

    # Recursively sort first n-1 elements
    recursive_insertion_sort(arr, n - 1)

    # Insert the last element at its correct position in sorted array
    last = arr[n - 1]
    j = n - 2

    # Shift elements greater than last
    while j >= 0 and arr[j] > last:
        arr[j + 1], arr[j] = arr[j], arr[j+1]
        j -= 1

    return arr
    


arr = [2,4,5,8,4,3] 
print(recursive_insertion_sort(arr))
