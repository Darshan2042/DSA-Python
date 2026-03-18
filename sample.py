# n = int(input("Enter size of the arr"))
# arr = list(map(int,input().split()))

# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] +=1
#     else:
#         freq[num] = 1

# result = []
# for num  in freq:
#     if freq[num] % 2 == 0:
#         result.append(num)

# print(result)


# n = input()
# vowle = 0
# consonants = 0
# digits = 0
# sp_char = 0

# vowles = ['a','e','i','o','u','A','E','I','O','U']
# digit = ['0','1','2','3','4','5','6','7','8','9']
# sp_chars = ['!','@','#','$','%','^','&','*',]

# for ch in n:
#     if ch in vowles:
#         vowle +=1
#     elif ch in digit:
#         digits +=1
#     elif ch in sp_chars:
#         sp_char +=1
#     else:
#         consonants +=1

# print(vowle,consonants,digits,sp_char)





def prime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
    
def print_prime(n):
    for i in range(1,n+1):
        if prime(i):
            print(i)

n = 100
print(print_prime(n))