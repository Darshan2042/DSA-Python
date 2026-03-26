def armstrong(n):
    org = n
    temp = n
    digits = 0
    while temp > 0:
        digits += 1
        temp = temp // 10
    total  = 0
    while n > 0:
        digit = n % 10
        total += digit**digits
        n = n// 10
    if org == total:
        return True
    return False


n = int(input())
print(armstrong(n))