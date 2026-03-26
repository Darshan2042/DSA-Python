def sort(arr):
    arr.sort(reverse  = True)
    return arr


n = int(input())
arr  = list(map(int , input().split()))
# arr = []
# for i in range(n):
#     res = int(input())
#     arr.append(res)

print(sort(arr))