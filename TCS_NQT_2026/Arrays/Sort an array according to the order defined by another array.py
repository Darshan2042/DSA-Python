# Sort an array according to the order defined by another array

def sort_by_order(arr1, arr2):
    result = []

    for i in arr2:
        for j in arr1:
            if j == i:
                result.append(j)

    remaining = []
    for i in arr1:
        if i not in arr2:
            remaining.append(i)

    remaining.sort()

    return result + remaining


arr1 = [2,1,2,5,7,1,9,3,6,8,8]
arr2 = [2,1,8,3]

print(sort_by_order(arr1, arr2))