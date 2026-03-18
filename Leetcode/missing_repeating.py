
# Time complexity is O(n^2)
# Space complexity is O(1)
# def missing_repeating(nums):
#     for i in range(1,len(nums)+1):
#         count = 0
#         for j in range(len(nums)):
#             if nums[j]==i:
#                 count += 1
#         if count == 2:
#             print("repeating number is ",i)
#         elif count == 0:
#             print("missing number is ",i)

# arr = [1,2,3,4,4,6]
# missing_repeating(arr)







# Time complexity = O(n)
# space complexity = O(n)
def missing_repeating(nums):
    n = len(nums)
    repeating = -1
    missing = -1
    arr = [0] * (n + 1)
    for i in range(len(nums)):
        arr[nums[i]] +=1
    for i in range(1,len(nums)):
        if arr[i] == 2:
            repeating = i
        elif arr[i] == 0:
            missing = i
        if repeating != -1 and missing != -1:
            break
    return missing,repeating


arr = [1,2,3,4,4,6]
print(missing_repeating(arr))


            