# Sum of digits of a number.

def sum_digit(n):
    sum_digit = 0
    while n >0 :
        digit = n % 10
        sum_digit += digit
        n = n // 10
    return sum_digit


print(sum_digit(1123))
        