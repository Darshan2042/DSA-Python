def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr = [10,2,20,50,40,60,80,70,60,40,10,50,3,0,1]
selectionsort(arr)
print(arr)