# Program to add two fractions.
################################### CHAT-GPT Copy ##################
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def add_fraction(a, b, c, d):
    numerator = a * d + b * c
    denominator = b * d

    # simplify
    g = gcd(numerator, denominator)

    numerator //= g
    denominator //= g

    return numerator, denominator


# Example
a, b = 1, 2
c, d = 3, 4

num, den = add_fraction(a, b, c, d)
print(f"{num}/{den}")