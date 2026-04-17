# 1.Start from the first position
# 2.Find the smallest element in the whole array
# 3.Swap it with the first position
# 4.Move to next position
# 5.Again find smallest from remaining array
# 6.Swap it to correct position
# 7.Repeat until array is sorted

# Time Complexity:
#  Best Case: O(n²)
#  Average Case: O(n²)
#  Worst Case: O(n²)

# Space Complexity:
#  O(1)  (in-place sorting)
def selectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)-1):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

arr = [29,443,23,2,4,23,32,3,42,3,423,23,23,2424,232]
print(selectionSort(arr))