def palindrome( n ):
    if n < 0:
        return False
    rev = 0
    original = n
    while n > 0:
        digit = n % 10
        rev = rev *10 + digit
        n = n //10
    return rev == original
    
n = 955285
abs =palindrome(n)
print(abs)

