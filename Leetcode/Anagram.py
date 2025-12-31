def anagram(s,t):
    if len(s) != len(t):
        return False
    
    freq = set(s)

    for ch in freq:
        if s.count(ch) != t.count(ch):
            return False
    return True
    

s = "anagram"
t = "anagrams"
ana = anagram(s,t)
print(ana)