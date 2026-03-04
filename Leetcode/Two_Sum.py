# def two_sum(arr,target):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] + arr[j] == target:
#                 return arr[i] , arr[j]

def two_sum(nums,target):
    dist = {}
    for i,num in enumerate(nums):
        add = target - num
        if add in dist:
            return [dist[add], i]
        dist[num] = i
            
arr = [2,5,45,72,58,25,5,5,548,55]
print(two_sum(arr,target = 74))