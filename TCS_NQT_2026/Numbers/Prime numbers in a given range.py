# Prime numbers in a given range.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def prime_range(start,end):
    for num in range(start,end+1):
        if is_prime(num):
            print(num,end = " ")

prime_range(1,100)
    