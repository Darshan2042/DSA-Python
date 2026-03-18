#Find the largest number in an array

def largest(arr):
    lar = arr[0]
    for i in range(1,len(arr)):
        if lar < arr[i]:
            lar = arr[i]
    return lar

arr = [2,5,7,8,9,20,5,0,40,50,50,5000]
print(largest(arr))