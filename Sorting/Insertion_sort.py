# 1.Start from index 0
# 2.For each element, set j = i
# 3.Compare current element with previous element (nums[j-1])
# 4.If previous element is greater → swap them
# 5.Move one step left (j--)
# 6.Repeat until correct position is found or j = 0
# 7.Continue for all elements

# Time Complexity
# Best Case: O(n) → already sorted
# Average Case: O(n²)
# Worst Case: O(n²)

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

arr = [29,443,23,2,4,23,32,3,42,3,423,23,23,2424,232]
print(insertion_sort(arr))
