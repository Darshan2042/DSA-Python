# Second Smallest and Second Largest element in an array
def second_min(arr):
    first_min = float("inf")
    sec_min = float("inf")
    for num in arr:
        if num < first_min:
            sec_min = first_min
            first_min = num
        elif  num < sec_min:
            sec_min = num
    return sec_min

def second_max(arr):
    first_max = float("-inf")
    second_max = float("-inf")
    for num in arr:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
    return second_max

arr = [10,20,30,40,50,60,2,5,4,6]
print(second_min(arr))
print(second_max(arr))
