#Find the first non-repeating character in a string.

def string(s):
    dist = {}
    for ch in s:
        if ch in dist:
            dist[ch] += 1
        else:
            dist[ch] = 1

    for ch in s:
        if dist[ch] == 1:
            return ch
    return None

s = "abcabababbabac"
print(string(s))