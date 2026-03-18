#Average of all elements in an array

def average(arr):
    result = 0
    for num in arr:
        result += num
    avg = result/len(arr)   # we can use // in this question (floor division)
    return avg

arr = [10,20,30,40,50,60,70]
print(average(arr))