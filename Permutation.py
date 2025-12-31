# import itertools

# data = [1,2,3]
# perms = list(itertools.permutations(data))
# for p in perms:
#     print(p)

def permute(arr,left,right,res):
    if left == right:
        res.append(arr.copy())
    else:
        for i in range(left , right):
            arr[left] , arr[i] = arr[i] , arr[left]
            permute(arr , left + 1 , right , res)
            arr[left] , arr[i] = arr[i] , arr[left]
arr = [1,2,3]
s = len(arr)
output = []
permute(arr , 0 , s , output)
print(output)