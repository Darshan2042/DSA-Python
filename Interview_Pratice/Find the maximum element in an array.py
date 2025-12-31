#Find the maximum element in an array.
arr = [12,5,8,7,5,45,45,14,2,5,15]
max_element = arr[0]

for i in range(1,len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]

print(max_element)
