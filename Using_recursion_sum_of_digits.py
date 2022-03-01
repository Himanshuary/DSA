def Sumofdigits(n):
    if n==0:
        return 0
    else:
        return int(n%10) + Sumofdigits(int(n//10))
    
print(Sumofdigits(111))