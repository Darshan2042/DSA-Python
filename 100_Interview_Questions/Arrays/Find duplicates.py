def findDuplicates(nums):
    dist = {}                                                   #Time Complxity = O(n)
    for num in nums:                                            #Space Complexity = O(n)
        if num in dist:
            dist[num] += 1
        else:
            dist[num] = 1
    li = []
    for num in dist:
        if dist[num] > 1:
            li.append(num)
    return li

# This appraoch only for the twice exsting numbers.
    # seen = set()
    # li = []
    # for num in nums:
    #     if num not in seen:
    #         seen.add(num)
    #     else:
    #         li.append(num)
    # return li

nums = [10,20,30,40,50,10,30]
print(findDuplicates(nums))