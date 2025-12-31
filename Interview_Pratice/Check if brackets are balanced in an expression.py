#Check if brackets are balanced in an expression.

def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in expression:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
expr = input("Enter an expression: ")
if is_balanced(expr):
    print("Brackets are balanced ")
else:
    print("Brackets are NOT balanced")
