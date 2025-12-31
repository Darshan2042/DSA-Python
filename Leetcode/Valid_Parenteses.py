#LEETCODE PROBLEM 20

def is_valid(s):
    stack = []
    bracket = {")":"(","}":"{","]":"["}

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack[-1] != bracket[ch]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_valid(")({[({{}})(()]})"))
