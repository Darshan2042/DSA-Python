
######################## BRUTE FORCE ############################## 
# def subset(arr):
#     r = [[]]
#     for n in arr:
#         new_subset = []
#         for s in r:
#             new_subset.append(s + [n])
#         r.extend(new_subset)
#     return r
# arr = [1,2,3]
# all_subset = subset(arr)
# print(all_subset)

############################ BACKTRACK ##############################
def subset(nums):
    result = []
    def backtrack(start , path):
        result.append(path[:])
        for i in range(start , len(nums)):
            path.append(nums[i])
            backtrack(i + 1 ,path)
            path.pop()
    backtrack(0,[])
    return result
nums = [1,2,3]
all_subset = subset(nums)
print(all_subset)

