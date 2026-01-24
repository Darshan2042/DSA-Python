def product(nums):          
    n = len(nums)                      # find the length of the array
    ans = [1] * n                      # create result array filled with 1
    left = 1                           # stores product of elements to the left
    for i in range(n):                 # loop from left to right
        ans[i] = left                  # store left product for current index
        left *= nums[i]                # update left by multiplying current element

    right = 1                          # stores product of elements to the right
    for i in range(n-1, -1, -1):       # loop from right to left
        ans[i] *= right                # multiply with right product
        right *= nums[i]               # update right by multiplying current element
    return ans                         # return final result array

nums = [1,2,3,4]                
print(product(nums))                  