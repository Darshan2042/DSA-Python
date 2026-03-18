# Find the median of the given array
def median(arr):
    arr.sort()
    n = len(arr)
    result = n//2
    return arr[result]


def median_even_odd(arr):
    arr.sort()
    n = len(arr)
    if n % 2 ==1:
        return arr[n//2]
    else:
        return (arr[n//2 - 1] + arr[n//2]) / 2

arr = [50,6,80,200,60,50] 
print(median_even_odd(arr))