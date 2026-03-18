# Maximum product subarray in an array

def max_product(arr):
    max_sum = float("-inf")
    for i in range(len(arr)):
        curr_sum  = 1
        for j in range(i,len(arr)):
            curr_sum *= arr[j]
            max_sum = max(curr_sum,max_sum)
    return max_sum

arr = [3,-4,5,4,-1,7,-8]
print(max_product(arr))