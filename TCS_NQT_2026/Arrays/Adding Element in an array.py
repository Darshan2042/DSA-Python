# Adding Element in an array
def adding_element(arr,pos,element):
    arr.append(0)
    for i in range(len(arr)-1,pos,-1):
        arr[i] = arr[i-1]

    arr[pos] = element
    return arr

arr = [20,40,50,60,70]
pos = 3
element = 55
print(adding_element(arr,pos,element))