# 1.Start with the full array
# 2.Divide the array into two halves
# 3.Keep dividing until each part has only one element
# 4.Start merging the small parts
# 5.While merging:
# 6.Compare elements from both halves
# 7.Put the smaller one into a temporary list
# 8.Add remaining elements (if any)
# 9.Copy the sorted list back to original array
# 10.Repeat until full array is sorted

# Time Complexity
#     Best Case: O(n log n)
#     Average Case: O(n log n)
#     Worst Case: O(n log n)
# Space Complexity
#     Every Case: O(n)


def ms(arr, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    ms(arr, low, mid)
    ms(arr, mid + 1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

arr = [80, 40, 20, 1, 2, 50, 3, 4]
ms(arr, 0, len(arr) - 1)
print(arr)