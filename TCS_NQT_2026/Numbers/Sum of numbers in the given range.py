# Sum of numbers in the given range.

def sum_of_numbers(n):
    res = 0
    for i in range(1,n+1):
        res += i
    return res

print(sum_of_numbers(100))