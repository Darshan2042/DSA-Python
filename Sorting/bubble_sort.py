# 1.Start from the first element
# 2.Compare it with the next element
# 3.If first is bigger → swap
# 4.Move one step ahead and repeat
# 5.After one round, the biggest number goes to the end
# 6.Repeat the process for remaining elements

# Time Complexity:
#  Best Case: O(n)   (when array is already sorted)
#  Average Case: O(n²)
#  Worst Case: O(n²)

# Space Complexity:
#  O(1)  (in-place sorting)

def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr = [29,443,23,2,4,23,32,3,42,3,423,23,23,2424,232]
print(bubblesort(arr))

