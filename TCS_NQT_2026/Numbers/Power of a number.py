# Power of a number.

def power_number(a,b):
    result = 1
    for i in range(b):
        result = result * a
    return result
        
print(power_number(2,3))