## Using Recursion

def reverse(i, arr, n):
    if i>=(n//2):
        return arr
    
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return reverse(i+1, arr, n)
    

arr = [2,3,5,8,3] 
print(reverse(0, arr, 5))
