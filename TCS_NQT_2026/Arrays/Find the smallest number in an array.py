#Find the smallest number in an array
def minimum(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min

arr = [2,4,6,5,7,8]
print(minimum(arr))