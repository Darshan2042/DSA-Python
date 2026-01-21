def threesum(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]+ nums[j]+ nums[k]== target:
                    tri = sorted([nums[i],nums[j],nums[k]])
                    if tri not in res:
                        res.append(tri)
    return res
                
nums=[12,25,14,25,14,1,85,58,552,55,2,5,2,4,2,5,44,52,45,45,45,4,4,5,45,4,55]
target = 11
print(threesum(nums,target))
