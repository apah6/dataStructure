def check_parentheses(expression:str) -> bool:
    stack = []

    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(check_parentheses("("))
print(check_parentheses("( )"))
print(check_parentheses("( ) )"))
print(check_parentheses(")"))