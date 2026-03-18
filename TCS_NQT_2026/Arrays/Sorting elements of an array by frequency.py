# Sorting elements of an array by frequency

def frq_sort(arr):
    dist = {}
    for num in arr:
        if num in dist:
            dist[num] += 1
        else:
            dist[num] = 1
    result = []
    for num in sorted(dist , key= dist.get):
        result += [num] * dist[num]
    return result


arr = [50,50,40,50,960,10,10,10,10,10,2,2,30,50]
print(frq_sort(arr))