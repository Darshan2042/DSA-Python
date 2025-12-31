def anagram(s , t):
    # if len(s) != len(t):
    #     return False
    # char = set(s)
    # for ch in char:
    #     if s.count(ch) != t.count(ch):
    #         return False
    # return True
    if sorted(s) == sorted(t):
        return True
    return False
s = "anagram"
t = "nagaram"
print(anagram(s,t))

s = "rat"
t = "car"
print(anagram(s,t)) 
