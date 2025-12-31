#Check if two strings are anagrams

s = "anagram"
t = "aganram"
def anagram(s,t):
    if len(s) != len(t):
        return False
    frequency_count = set(s)
    print(sorted(frequency_count))
    for i in frequency_count:
        if s.count(i)== t.count(i):
            return True
    return False
print(anagram(s,t))

def anagrams(s,t):
    if len(s) != len(t):
        return False
    if sorted(s) == sorted(t):
        return True
    else:
        return False
    
print(anagrams(s,t))