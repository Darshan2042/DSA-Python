def even_odd(n):
    even  = 0
    odd = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n // 10
    return even , odd
    

n = int(input())
even,odd = even_odd(n)
print(f"Even = {even}")
print(f"Odd = {odd}")