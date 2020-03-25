# Written: 25-Mar-2020

t = int(input())        # number of expressions

for i in range(t):
    exp = input()       # original expression
    operators =  list() # storing operators +, -, *, /, ^ (priority from the lowest to the highest)
    form = ''           # RPN form

    for char in exp:
        if char == '(':
            pass                        # skip
        elif char == ')':
            if len(operators) != 0:
                form += operators.pop() # reset and push operators to form
        elif 97 <= ord(char) <= 123:    # operands found (lowercase a-z)
            form += char
        else:                           # operators found
            operators.append(char)
    print(form)                         # print expression
