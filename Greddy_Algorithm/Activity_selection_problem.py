def activity_Selection(start , end , n):
    activites = sorted(zip(start , end),key=lambda x:x[1])
    count = 0
    last_end = 0
    for s,e in activites:
        if s > last_end:
            count +=1
            last_end = e
    return count
start = [1,3,0,5,8]
end = [2,4,6,7,9]
n = len(start)
print(activity_Selection(start , end , n))