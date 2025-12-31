#Count vowels and consonants in a string.

def count(s):
    vowels = 0
    consonents = 0
    stack = ["a","e","i","o","u"]
    for i in s.lower():
        if i.isalpha():
            if i in stack:
                vowels += 1
            else:
                consonents += 1

    return vowels , consonents

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabc"
print(count(s))