nums = int(input())  # size
arr = []

for i in range(nums):
    arr.append(int(input()))  # input

def insertion_sort(nums):
    for i in range(1, len(nums)):  # start from 1
        j = i  # current index
        
        while j > 0 and nums[j-1] > nums[j]:  # compare left
            nums[j], nums[j-1] = nums[j-1], nums[j]  # swap
            j -= 1  # move left
    
    return nums

print(insertion_sort(arr))  # output


# Dry Run:
# Input: 64 25 12 22 11

# Pass 1 → [25, 64, 12, 22, 11]
# Pass 2 → [12, 25, 64, 22, 11]
# Pass 3 → [12, 22, 25, 64, 11]
# Pass 4 → [11, 12, 22, 25, 64]

# Final → [11, 12, 22, 25, 64]