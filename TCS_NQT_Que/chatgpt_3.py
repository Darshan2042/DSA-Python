def unique(arr):
    seen = set()
    res = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            res.append(num)
    return res

arr = list(map(int,input().split()))
print(unique(arr))
