#Merge two sorted arrays into one.
arr1 = [5,10,15,20,25]
arr2 = [6,12,18,24,58,74]
res = []
fp = 0
bp = 0
while fp < len(arr1) and bp < len(arr2): #Comapre the each the element
    if arr1[fp] < arr2[bp]:
        res.append(arr1[fp])
        fp += 1
    else:
        res.append(arr2[bp])
        bp += 1
while fp < len(arr1): # add remaing element in array
    res.append(arr1[fp])
    fp += 1
while bp < len(arr2):
    res.append(arr2[bp])
    bp += 1
print(res)