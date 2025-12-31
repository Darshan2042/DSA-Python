#Convert a binary number to decimal.

def decimal(n):
    dec = 0
    power = 0
    while n > 0:
        digit = n % 10
        dec += digit * (2 ** power)
        n //= 10
        power += 1
    return dec

n = 100
print(decimal(n))