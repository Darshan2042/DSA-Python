# Sum of first N natural numbers.

def sum_of_natural_numbers(n):
    result = 0
    for i in range(1,n+1):
        result += i

    return result


n = 50
print(sum_of_natural_numbers(n))