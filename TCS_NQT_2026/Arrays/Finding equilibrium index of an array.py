# Finding equilibrium index of an array

def equlibrium(arr):
    total  = sum(arr)
    print(total)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total  - left_sum - arr[i]
        if left_sum == right_sum:
            return i

        left_sum += arr[i]
    return -1

# Logic in Simple Words
# First calculate total sum of the array.
# Start traversing the array.
# Keep track of left sum.
# Calculate right sum using:

arr = [-7, 1, 5, 2, -4, 3, 0]
print(equlibrium(arr))