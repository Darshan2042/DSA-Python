number = 321123
def reverse(number):
    org = number
    rev = 0
    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10
    return rev == org

print(reverse(number))