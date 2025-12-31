def Mergesort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2
    left = Mergesort(arr[:mid])
    right = Mergesort(arr[mid:])

    return merge(left , right)
def merge(left,right):
    r = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            r.append(left[i])
            i += 1
        else:
            r.append(right[j])
            j += 1

    r.extend(left[i:])
    r.extend(right[j:])
    return r

arr = [11,3,2,4,6,21,65,35,94,75,26,32]
print(Mergesort(arr))