n = int(input())
arr = []
for _ in range(n):
    res = int(input())
    arr.append(res)
dist = {}
for num in arr:
    if num in dist:
        dist[num] += 1
    else:
        dist[num]= 1

res = max(dist.values())
for key in dist:
    if dist[key] == res:
        print("this is answer",key)
