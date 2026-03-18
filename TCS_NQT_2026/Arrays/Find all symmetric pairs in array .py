#  Find all symmetric pairs in array.

def symmetric(arr):
    dist = {}
    for a,b in arr:
        if b in dist and dist[b] == a:
            print((a,b))
        else:
            dist[a] = b

pairs = [(1,2),(3,4),(5,7),(2,1)]
symmetric(pairs)