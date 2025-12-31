#Count the frequency of elements in an array.

arr = [10,20,10,10,5,50,50,40,40,50,80,70,0,58]

dict = {} #### Dictonary with element and their count

for num in arr:  ## each element in arr are interate
    if num in dict:   ## if the element already in the dictonary 
        dict[num] += 1  ## just increase their count
    else:
        dict[num] = 1   ## if the element are not there the count will start from 1
print(dict) 
        