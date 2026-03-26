def chatgpt(arr):
    first = float("-inf")
    second = float("-inf")
    for num in arr:
        if num > first :
            second =  first
            first = num
        elif num > second and num != first :
            second = num
    if second != float("-inf"):
        return second
    return -1





n = int(input())
arr = []
for _ in range(n):
    res = int(input())
    arr.append(res)
print(chatgpt(arr))