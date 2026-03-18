# Replace all 0s with 1s in a given intege.

def replace_zero(n):
    result = 0
    place = 1

    while n > 0:
        digit = n % 10

        if digit == 0:
            digit = 1

        result += digit * place
        place *= 10
        n //= 10

    return result


print(replace_zero(1020)) 