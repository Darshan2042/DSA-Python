def non_repeating(s):
    dist = {}
    for ch in s:
        if ch in dist:
            dist[ch] += 1
        else:
            dist[ch] = 1

    for ch in dist:
        if dist[ch] == 1:
            return ch
    return -1

s = input()
print(non_repeating(s))