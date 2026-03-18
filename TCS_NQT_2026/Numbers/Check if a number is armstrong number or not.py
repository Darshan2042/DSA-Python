# Check if a number is armstrong number or not.

def armstrong(n):
    org = n
    digits = len(str(n))
    rev = 0
    while n > 0:
        digit = n % 10
        rev += digit ** digits
        n = n //10
    return org == rev 

n = 153
print(armstrong(n))