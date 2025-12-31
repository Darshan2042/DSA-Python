def palindrome_string(s):
    if len(s) == 1:  # base case
        return True
    if s[0]!=s[-1]:
        return False
    return palindrome_string(s[1:-1])
        
s = "hello"
print(palindrome_string(s))  

