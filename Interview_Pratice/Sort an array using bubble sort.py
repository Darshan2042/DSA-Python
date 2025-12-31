#Sort an array using bubble sort.

arr = [12,45,74,84,5,8,54,2,59,88]
n = len(arr)
for i in range(n- 1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j] , arr [ j+1] = arr[ j+1] , arr[j]
print(arr)