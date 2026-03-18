# Maximum and Minimum digit in a number.

def max_min_digit(n):
    max_digit = 0
    min_digit = 0

    while n > 0:
        digit = n % 10

        if digit > max_digit:
            max_digit = digit
        if digit < min_digit:
            min_digit = digit
        
        n = n // 10

    return max_digit , min_digit

n = 1234565
print(max_min_digit(n))