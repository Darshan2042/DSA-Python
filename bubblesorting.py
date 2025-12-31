arr = [10,20,30,35,50,10,50,8,50]
def bubble(arr):
    arr1 = len(arr)
    for i in range(arr1):
        for j in range(0,arr1-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1]= arr[j+1] , arr[j]
                print(arr)
    return arr

print(bubble(arr))