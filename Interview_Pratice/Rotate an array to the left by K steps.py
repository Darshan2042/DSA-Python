#Rotate an array to the left by K steps.

arr = [1,2,3,4,5,6,7,8,9]
k = 2
n = len(arr)
k = k % n   
print(arr[k:] + arr[:k]) ## for left rotate
print(arr[-k:] + arr[:-k]) ## for right rotate

