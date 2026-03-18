# Rotate array by K elements – Block Swap Algorithm

def rotate_array(arr,k):
    n = len(arr)
    k = k%n
    arr[:] = arr[:-k] + arr[-k:]
    return arr

arr = [10,20,30,40,50,60,70]
k=3
print(rotate_array(arr,k))
