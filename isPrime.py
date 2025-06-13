class Solution:
    def isPrime(self, n):
        #your code goes here
        i = 2
        val = False
        while(i<int(math.sqrt(n)+1):
            if n%i != 0:
                val = False
            else:
                val = True

        return val
