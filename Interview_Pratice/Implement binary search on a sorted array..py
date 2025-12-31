#Implement binary search on a sorted array.

def binary(arr,target):
    low = 0
    high = len(arr)-1
    while low <= high :
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return -1
arr = [10,20,30,40,45,54,78,100]
target = 30
result = binary(arr,target)
print(f"Index Number{result}  Target Numbet{target}")