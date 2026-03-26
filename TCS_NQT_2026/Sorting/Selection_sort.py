nums = int(input("Enter Number of Elements: "))  # input size
arr = []
for i in range(nums):
    arr.append(int(input()))  # take elements
def selection(nums):
    for i in range(len(nums)):  # outer loop
        min_index = i  # assume min
        for j in range(i+1, len(nums)):  # find min
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]  # swap
    return nums

print(selection(arr))  # output