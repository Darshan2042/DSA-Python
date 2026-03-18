# Replace each element of the array by its rank in the array

def rank(arr):
    sorted_arr = sorted(arr)
    dist ={}
    r = 1
    for num in sorted_arr:
        if num not in dist:
            dist[num] = r
            r += 1
    for i in range(len(arr)):
        arr[i] = dist[arr[i]]
    return arr


arr = [10,50,4,50,60,8,40,20]
print(rank(arr))