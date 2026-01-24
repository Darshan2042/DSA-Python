def max_sum(nums):
    curr = nums[0]                      # current subarray sum starting from first element
    max_sum = nums[0]                   # stores maximum sum found so far

    for i in range(1, len(nums)):       # loop through array from second element
        curr = max(nums[i], nums[i] + curr)  # decide: start new subarray or extend previous one
        max_sum = max(max_sum, curr)    # update maximum if current sum is larger

    return max_sum                      # return final maximum subarray sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sum(nums))