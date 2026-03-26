def  sum_digit(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n//10
    return total

n = int(input())
print(sum_digit(n))