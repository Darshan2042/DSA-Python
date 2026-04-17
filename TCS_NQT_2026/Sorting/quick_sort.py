# 1.Start with low = 0 and high = n-1
# 2.Check if low < high (more than 1 element)
# 3.Choose pivot element (arr[low] in your code)
# 4.Take two pointers:
#    i = low, j = high
# 5.Move i forward until element > pivot
# 6.Move j backward until element ≤ pivot
# 7.If i < j → swap arr[i] and arr[j]
# 8.Repeat steps 5–7 until i ≥ j
# 9.Swap pivot (arr[low]) with arr[j]
# 10.Now pivot is at correct position
# 11.Apply same steps on left part (low to pIndex-1)
# 12.Apply same steps on right part (pIndex+1 to high)
# 13.Repeat until array is sorted
# Time Complexity
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n²)
# Space Complexity
# O(log n) (recursion stack)

def qs(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)

        qs(arr, low, pIndex - 1)
        qs(arr, pIndex + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = [40, 70, 50, 10, 2, 5, 60]
qs(arr, 0, len(arr) - 1)
print("Sorted array:", arr)