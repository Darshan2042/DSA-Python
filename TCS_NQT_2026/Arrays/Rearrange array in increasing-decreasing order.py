# #Rearrange array in increasing-decreasing order

# def rearrange_array(arr):
#     arr.sort()
#     mid = len(arr)//2
#     result = []
#     for i in range(mid):
#         result.append(arr[i])
#     for i in range(len(arr)-1,mid-1,-1):
#         result.append(arr[i])

#     return result


# arr =[20,10,20,50,40,50,80,580,8]
# print(rearrange_array(arr))


def rearrange_array(arr):
    n = len(arr)
    for i in range(len(arr)):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    print(arr)

    for i in range(len(arr)):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print(arr)

arr =[20,10,20,50,40,50,80,580,8]
rearrange_array(arr)