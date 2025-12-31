def two_sum(arr , target):
    for i in range(len(arr)):
        for j in range(i+ 1,len(arr)):
            if arr[i] + arr[j]  == target:
                return [i,j]
arr = [20,10 , 50 , 60 , 40 ,  80]
target = 120

result=two_sum(arr,target)
print(result)