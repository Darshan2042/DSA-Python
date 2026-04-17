n = int(input())
arr  = list(map(int,input().split()))

sum_odd = 0
count  = 0
for num in arr:
    if num % 2 != 0:
        sum_odd += num
        count += 1

# instead of this code i write this code....
# avg = sum_odd / count ..... that's why the error are occur..
if count > 0:
    avg = sum_odd / count
else:
    avg = 0

print(sum_odd,count,avg)
