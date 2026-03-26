nums = int(input())  # size
arr = []

for i in range(nums):
    arr.append(int(input()))  # input

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):  # passes
        for j in range(0, n-i-1):  # compare
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap
    
    return arr

print(bubble_sort(arr))  # output


# Dry Run:
# Input: 64 25 12 22 11

# Pass 1 → [25, 12, 22, 11, 64]
# Pass 2 → [12, 22, 11, 25, 64]
# Pass 3 → [12, 11, 22, 25, 64]
# Pass 4 → [11, 12, 22, 25, 64]

# Final → [11, 12, 22, 25, 64]