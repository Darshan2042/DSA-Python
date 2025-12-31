#Find the largest sum subarray.
def subarray(arr):
    max_sum = arr[0]   # max_sum will be the first element 
    curr_sum = 0       # current_sum will be 0
    for n in arr:
        curr_sum += n   # in current sum and new element from arr
        max_sum = max(max_sum,curr_sum)  # in the max_sum variable store a max_sum or curr_sum highest value
        if curr_sum < 0: # check the current sum in negative or not
            curr_sum = 0 # if current sum will be zero the current_sum will be reset
    return max_sum  # return max_sum

arr = [25,45,47,-1,1,28,25,-25,82,5]
print(subarray(arr))
