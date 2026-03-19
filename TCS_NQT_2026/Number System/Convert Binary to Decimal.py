# Convert Binary to Decimal

def binary_to_decimal(binary):
    decimal = 0
    power = 0

    while binary > 0:
        digit = binary % 10
        decimal += digit * (2 ** power)
        binary = binary // 10
        power += 1

    return decimal

print(binary_to_decimal(111111111))