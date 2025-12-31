#Check if a string is a palindrome.
##############Using In Slicing
s = "abba"
org = s
result = s[::-1]
print(s==result)

#Logic
fp = 0
bp = len(s)-1
s = list(s)
while fp < bp:
    s[fp] , s[bp]= s[bp] , s[fp]
    fp += 1
    bp -= 1
result = "".join(s)
if org == result :
    print(True)
else:
    print(False)