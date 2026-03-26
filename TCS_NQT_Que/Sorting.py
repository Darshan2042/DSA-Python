nums = list(map(int, input().split()))

arr = []
for i in range(0, len(nums), 2):
    arr.append((nums[i], nums[i+1]))

arr.sort()
print(arr)