def missing(arr):
    n = len(arr)
    sum_arr = sum(arr)
    a = n*(n+1)//2
    res = a - sum_arr
    return res

arr = list(map(int , input().split()))
print(missing(arr))