# Remove duplicate elements from an array.

arr = [10,2,82,5,4,5,1,45,1,5,15,5,5,5,5,2,2,2]

print(list(set(arr)))

##########

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)
    else:
        None
print(unique)