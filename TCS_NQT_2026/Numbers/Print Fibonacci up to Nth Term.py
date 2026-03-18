# Print Fibonacci up to Nth Term.

def fabonacci_number(n):
    if n <= 1:
        return 1
    else:
        a = 0
        b = 1
        seen = []
        for i in range(n):
            seen.append(a)
            a,b = b , a+b
        return seen

n = 10
print(fabonacci_number(n))            