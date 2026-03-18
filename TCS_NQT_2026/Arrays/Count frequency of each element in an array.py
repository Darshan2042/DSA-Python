def count_frq(arr):
    dist = {}
    for num in arr:
        if num in dist:
            dist[num] +=1
        else:
            dist[num] = 1

    return dist

arr = [10,10,20,40,50,50,50,50,50,50,00,505]
result   = count_frq(arr)



for key , value in result.items():
    print(f"{key} = {value}")
