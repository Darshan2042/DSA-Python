#Find the missing number in a range from 1 to N.
## n * (n+1) // 2   - sum(element)

arr = [1,2,3,4,5,6,8,9,10,11,12,13,14,15] # Given Array
n = 15                                    # Number range
 
total = n * (n+1) // 2   # formula
adding  = sum(arr)       # sum of the array

missing =  total - adding  ## find missing Number
print(missing)