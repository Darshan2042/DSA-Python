# Print all prime factors of the given number.

def is_prime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count +=1
    if count == 2:
        return True
    else:
        return False

def even_prime(n):
    seen = []
    for i in range(1,n+1):
        if n % i == 0:
            seen.append(i)
    for num in seen:
        if is_prime(num):
            print(num)

n = 12
print(even_prime(n))

    
