# Find all non-repeating elements in an array
def non_repeating(arr):
    dist ={}
    for num in arr:
        if num in dist:
            dist[num] +=1
        else:
            dist[num] = 1

    for num in dist:
        if dist[num] == 1:
            print(num)

arr = [10,20,30,50,40,10,20,50]
non_repeating(arr)
            