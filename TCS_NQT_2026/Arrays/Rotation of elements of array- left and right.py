# Rotation of elements of array- left and right

def left_rotation(arr , k):
    n = len(arr)
    k = k % n
    result = arr[k:] + arr[:k]
    return result

def right_rotation(arr , k):
    n = len(arr)
    k = k%n
    result = arr[-k:] + arr[:-k]
    return result

arr = [10,20,30,40,50]
print(right_rotation(arr , k = 2))