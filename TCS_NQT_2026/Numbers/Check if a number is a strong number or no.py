# Check if a number is a strong number or no.

# def fact(n):
#     org = n 
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact

# def strong_number(n):
#     org = n
#     total = 0

#     while n > 0:
#         digit = n % 10
#         total = total + fact(digit)
#         n = n // 10
#     return total == org

# n = 150
# print(strong_number(n))


def fact(n):
    fact = 1
    print(f"  Calculating factorial of {n}")
    
    for i in range(1, n + 1):
        fact *= i
        print(f"    {i}! step → fact = {fact}")
    
    return fact


def strong_number(n):
    org = n
    total = 0

    print(f"Checking number: {n}\n")

    while n > 0:
        digit = n % 10
        print(f"Extracted digit: {digit}")

        f = fact(digit)
        print(f"Factorial of {digit} = {f}")

        total += f
        print(f"Running total = {total}\n")

        n = n // 10

    print(f"Final Sum = {total}")
    print(f"Original Number = {org}\n")

    return total == org


n = 150

if strong_number(n):
    print("Result: Strong Number")
else:
    print("Result: Not a Strong Number")