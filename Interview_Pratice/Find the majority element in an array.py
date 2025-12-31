#Find the majority element in an array (if any).

def majority(arr):
    fre = {}
    for num in arr:
        if num in fre :
            fre[num] += 1
        else:
            fre[num] = 1

    for num in fre :
        if fre[num] > len(arr) // 2:
            return num
    return "No Majority Element"
arr = [2,15,4,85,5,5,25,5,5,5,8,8]
print(majority(arr))