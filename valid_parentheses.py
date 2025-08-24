def isValid(s: str) -> bool:
    stack = []
    parentheses_paris = {")" : "(", "]" : "[", "}" : "{"}
    
    for c in s:
        if c in parentheses_paris:
            if stack and stack[-1] == parentheses_paris[c]:
                stack.pop()
            else:
                return False
        
        else:
            stack.append(c)
            
    return len(stack) == 0

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid("([)]"))