#Remove duplicates from an unsorted array
arr = [60,40,80,70,90,60,40,80,85]
def remove_duplicates_unsorted_array(arr):
    seen = set()       # by using this set the time complexity will be O(n)
    unique = []
    for num in arr:
        if num not in seen:   # O(n2) because the if condition check compete unique list.
            unique.append(num)
            seen.add(num)

    return unique

print(remove_duplicates_unsorted_array(arr)) 