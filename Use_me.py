def two_sum(nums,target):
    dist  = {}
    for i , num in enumerate(nums):
        res = target - nums[i]

        if res in dist:
            return [dist[res],i]
        else:
            dist[num] =  i

arr = [10,20,30,200,50,40,5050,50]
target = 50
print(two_sum(arr,target))

