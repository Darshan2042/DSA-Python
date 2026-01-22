def max_profit(nums):
    buy = nums[0]                                               #Time Complexity = O(n)
    maximum = 0                                                 #Space Complexity = O(1)
    for i in range(len(nums)):
        if nums[i] < buy :
            buy = nums[i]
        else:
            maximum = max(maximum,nums[i] - buy)
    return maximum

nums =[7,6,4,3,1]
print(max_profit(nums))