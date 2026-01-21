def sumofevenandodd(nums):
    evensum = 0
    oddsum = 0
    for num in nums:
        if num % 2 == 0:
            evensum += num
        else:
            oddsum += num
    return evensum,oddsum

nums = [2,14,5,5,8,47,58,58,6,8,52,]
result_1,result_2 = sumofevenandodd(nums)
print("Sum of Even Numbers in list:",result_1)
print("sum of Odd Numbers in list:",result_2)