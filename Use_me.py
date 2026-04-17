# arr = [20,80,22,4,3,2,5,18,1]
# smallest_num = arr[0]
# for i in range(1,len(arr)):
#     if arr[i] > smallest_num:
#         smallest_num = arr[i]
# print(smallest_num)


# sum = 0
# n = 12345
# while n > 0:
#     digit = n%10
#     sum += digit
#     n //= 10
# print(sum)


def missing_number(arr):
    sum_arr = 0
    n = len(arr)
    for num in arr:
        sum_arr += num
    total= n*(n+1)//2
    return total - sum_arr
    

arr = [0,1,2,4,5,6,7]
print(missing_number(arr))
