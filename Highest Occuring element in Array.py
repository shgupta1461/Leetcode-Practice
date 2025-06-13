## Hashing

def mostFrequentElement(nums):
    freq = {}

    for i in range(len(nums)):
        if nums[i] in freq:
            freq[nums[i]] = freq[nums[i]] + 1
        else:
            freq[nums[i]] = 1
    max_key = max(dict(sorted(freq.items())), key=freq.get)

    return max_key

arr = [2,4,5,8,4, 3,3] 
print(mostFrequentElement(arr))
