# Check if a number is a perfect square.
import math
def sqaure(n):
    result  = int(math.sqrt(n))
    return result * result == n


def bruteforce(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        else:
            i += 1
    return False

n = 25
print(sqaure(n))
print(bruteforce(n))

