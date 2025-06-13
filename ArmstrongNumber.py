def isArmstrong(n):

    n1 = n
    power = len(str(n))
    rev = 0
    s = 0
    for i in range(power):
        num = n%10
        rev = rev*10 + num
        n = n//10
        s = s + pow(num, power)
        print(s)
        
    if s == n1:
        print(True)
        return True
    else:
        return False
    
isArmstrong(153)
