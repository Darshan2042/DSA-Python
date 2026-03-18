#  Search an element in an array

def serch_element(arr,ele):
    # for i in range(len(arr)):
    #     if arr[i] == ele:
    #         return i
    # return -1
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            low = mid+1
        else:
            high = mid-1
    return -1

arr = [10,20,30,40,50,60,70]
ele = 50
print(serch_element(arr,ele))