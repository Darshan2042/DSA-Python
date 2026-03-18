#Remove duplicates from a sorted array.

def remove_duplicate(arr):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i += 1
        arr[i] = arr[j]
    return i+1

arr = [10,10,20,30,30,40,50]
length = remove_duplicate(arr)
print(arr[:length])
print(length)