# Check if Array is a subset of another array or not 

def arr_subset(arr1,arr2):
    for num in arr2:
        if num not in arr1:
            return False
    return True



arr1 = [10,20,30,40,50,60]
arr2 = [20,40,60]
print(arr_subset(arr1 , arr2))