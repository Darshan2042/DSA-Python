# Factors of a given number.

def factors(n):
    seen = []
    for i in range(1,n+1):
        if n % i == 0:
            seen.append(i)

    return seen

# def factors(n):
#     for i in range(1,n+1):
#         if n % i == 0:
#             print(i)


n = 12
print(factors(n))