#Check if a number is an Armstrong number.

def armstrong(n):
    org = n                             # original number store in org variable
    digits = len(str(n))                # count the number of digits in n variable
    rev = 0                             # result variable will be zero
    while n > 0:                        # check the condition n in grater than zero
        digit = n % 10                  # get a last digit of n
        rev += digit ** digits          #in result variable add the digit power of digits
        n = n // 10                     ## remove the last digit from n

    return org == rev                   # check the original  and n is same or not
n = 153
print(armstrong(n))
