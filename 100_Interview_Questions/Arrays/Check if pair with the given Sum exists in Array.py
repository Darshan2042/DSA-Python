def twosum(nums,target):
    dist = {}                                                   #Time Complexity = O(n)
    i = 0                                                       #Space Complexity = O(n)
    while i < len(nums):
        num = nums[i]
        number = target - num
        if number in dist:
            return [dist[number],i]
        dist[num] = i
        i += 1
nums = [2,5,4,7,8]
target = 11
print(twosum(nums,target))