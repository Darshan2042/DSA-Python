def reverse(n):
    org = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev == org

n = int(input())
print(reverse(n))