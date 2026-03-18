# Check if the number is abundant number or not.

def abundant(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    
    if total > n :
        return " Abundant Number"
    return " Non abundant Number"

print(abundant(14))