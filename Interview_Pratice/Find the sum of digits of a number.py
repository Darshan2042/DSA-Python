#Find the sum of digits of a number.
n = 15
res = 0
while n > 0:
    digit = n % 10
    res = res + digit
    n //= 10
print(res)