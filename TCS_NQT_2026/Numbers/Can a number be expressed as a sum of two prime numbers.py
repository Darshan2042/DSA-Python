#  Can a number be expressed as a sum of two prime numbers .

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True


def check_sum_of_primes(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            print(f"{n} = {i} + {n - i}")
            return True
    return False


n = 10

if not check_sum_of_primes(n):
    print("Not possible")