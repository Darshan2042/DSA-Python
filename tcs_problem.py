# li = (7, 4, 8, 2, 9)
# count = 1
# for i in range(1,len(li)-1): 
#     if li[i] < li[i+1]:
#         count += 1
# print(count)

# n = 524
# product = 1
# for digit in str(n):
#     product *= int(digit)
# print(product)

arr = [1, 0, 1, 2, 0, 1,0]
C0 = arr.count(0)
C1 = arr.count(1)
C2 = arr.count(2)

list1 = [0]*C0 + [1]*C1 + [2]*C2
print(list1)