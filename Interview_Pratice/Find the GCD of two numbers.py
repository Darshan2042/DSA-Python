#Find the GCD of two numbers.

def GCD(n,m):
    while m != 0:
        n , m = m, n % m 
    return n
n = 1525
m = 150
print(GCD(n,m))