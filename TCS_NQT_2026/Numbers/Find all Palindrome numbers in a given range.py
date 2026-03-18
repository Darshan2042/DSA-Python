# Find all Palindrome numbers in a given range

def palindrome(n):
    org = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return org == rev

def palindrome_range(start , end):
    for num in range(start,end+1):
        if palindrome(num):
            print(num , end=" ")

print(palindrome_range(100,200))