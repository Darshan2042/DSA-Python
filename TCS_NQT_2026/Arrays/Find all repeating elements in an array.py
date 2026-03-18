# Find all repeating elements in an array.
def repeating_element(arr):
    seen  = set()
    repeated = set()
    for num in arr:
        if num in seen and num not in repeated:
            print(num)
            repeated.add(num)
        else:
            seen.add(num)
    return repeated


arr = [10,20,30,40,50,50,8,870,50,40,60]
repeating_element(arr)