def reverse_arr(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr

arr = [10,20,30,40,50,60,70,80]
print(reverse_arr(arr))
print(arr[::-1])