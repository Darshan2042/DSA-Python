arr = [1,2,3,4,5]
pre = [0]*len(arr)
pre[0]=arr[0]
for i in range(1,len(arr)):
    pre[i] = pre[i-1]+arr[i]
print(pre)