# Find the second largest element in an array.

arr = [12, 54, 4, 57, 47, 5, 48, 45, 7, 58, 25, 8]
#######Using Inbuild function
arr = list(set(arr))
arr.sort(reverse=True)
print(arr[1])

# logic
first = -1  # start with small number
second = -1 # start with small number
for num in arr:
    if num > first: # 12 > -1 ## 54 > 12  ### 4 > 54 Error
        second = first #-1  ## 12  
        first = num # 12  ## 54
    elif num > second:  ####################  4 > 12 Error
        second  = num
print(second)