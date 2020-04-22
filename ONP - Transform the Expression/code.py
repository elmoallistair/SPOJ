# Written: 25-Mar-2020
# https://www.spoj.com/problems/ONP/

t = int(input())

for i in range(t):
    exp = input()
    operators =  list()
    form = ''

    for char in exp:
        if char == '(':
            pass
        elif char == ')':
            if len(operators) != 0:
                form += operators.pop()
        elif 97 <= ord(char) <= 123:X
            form += char
        else:
            operators.append(char)
    print(form)
