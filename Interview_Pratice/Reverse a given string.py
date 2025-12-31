#Reverse a given string.
s = "abcdedf"
s = list(s)
st = 0
lt = len(s)-1
while st < lt:
    s[st] , s[lt] = s[lt] , s[st]
    st += 1
    lt -= 1
print("".join(s))