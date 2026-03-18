# Check if a number is palindrome or not.

def palindrome(n):
    org = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return org == rev

n = 12321
print(palindrome(n))