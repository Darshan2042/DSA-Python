def two_sum(nums,target):
    hash_set = {}
    for i,num in enumerate(nums):
        reaminder = target - num
        if reaminder in hash_set:
            return [reaminder,num]
        hash_set[num] = i

nums = [2,5,48,8,7,8,7,5,8,8,8,5,2,4,3,1]
target = 49
print(two_sum(nums,target))