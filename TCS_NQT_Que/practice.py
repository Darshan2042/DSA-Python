def discount(n):
    if n <  1000:
        discount = 0.05
    elif n < 5000:
        discount = 0.10
    else:
        discount = 0.15
    res = n - (n*discount)

    return res

n = int(input())
print(discount(n))