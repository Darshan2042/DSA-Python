def anagram(s,n):
    if len(s) != len(n):
        return False
    dist = {}
    for ch in s:
        if ch not in dist:
            dist[ch] = 1
        else:
            dist[ch] +=1
    
    for ch in n:
        if ch not in dist:
            return False
        dist[ch] -= 1
        if dist[ch] < 0:
            return False
    return True

s = input()
n = input()
print(anagram(s,n))