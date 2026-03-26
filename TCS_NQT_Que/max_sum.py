def max_sum(nums):
    curr_sum = nums[0]
    max_sum = nums[0]
    for i in range(1,len(nums)):
        curr_sum = max(curr_sum + nums[i],  nums[i])
        max_sum = max(curr_sum,max_sum)
    return max_sum

n =  int(input())
arr = []
for i in range(n):
    new = int(input())
    arr.append(new)

print(max_sum(arr))