# Check if a number is prime or not.

# def prime(n):
#     count = 0
#     for i in range(1,n+1):
#         if n%i == 0:
#             count += 1
#     if count == 2:
#         return True
#     False


def prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

n = 17
print(prime(n))