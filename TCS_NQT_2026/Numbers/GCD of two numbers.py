# GCD of two numbers.

def GCD(a,b):
    res = 1
    for i in range(1,min(a,b) + 1):
        if a % i == 0 and b % i ==0:
            res = i
    return res


print(GCD(12,18))