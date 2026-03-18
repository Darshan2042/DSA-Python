# LCM of two numbers.

def LCM(a,b):
    num = max(a,b)
    while True:
        if num % a == 0 and num % b == 0:
            return num
        num +=1

print(LCM(12,18))