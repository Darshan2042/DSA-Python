#Find the intersection of two arrays.
arr = [1,4,14,44,7]
arr1 = [5,4,14,44,8]

result  = (set(arr) & set(arr1))
print(result)

results = set(arr).intersection(set(arr1))
print(results)

#Brute force

result  = []
for n in arr:
    if n in arr1 and n not in result:
        result.append(n)

print("Brute Force approach",result)

# two pointer

arr.sort()
arr1.sort()

i = 0
j = 0
res =[]
while i < len(arr) and j < len(arr1):
    if arr[i]==arr1[j]:
        res.append(arr[i])
        i += 1
        j += 1
    elif arr[i] < arr1[j]:
        i +=1
    else:
        j += 1
print("Two Pointer Approach" , res)