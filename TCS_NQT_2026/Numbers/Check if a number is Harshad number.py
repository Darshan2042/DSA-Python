# Check if a number is Harshad number.

def harshad(n):
    org  = n
    sum_digit  = 0
    while n > 0:
        digit = n % 10
        sum_digit += digit
        n = n // 10
    
    if org % sum_digit == 0:
        return True
    return False


print(harshad(19))